from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
import asyncio
import re
import os
import httpx
import json
from rate_limiter import check_rate_limit
import models

router = APIRouter()

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=5, max_length=1000)

class ChatResponse(BaseModel):
    response: str
    severity: str
    applicableSections: list
    nextSteps: list
    disclaimer: str

# Retrieve Ollama configurations
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

def analyze_message(msg: str):
    msg_lower = msg.lower()
    
    # Initialize variables
    intent = "general"
    severity = "Information Only"
    applicable_sections = []
    next_steps = []
    response = ""
    disclaimer = "This is a simulated AI response from the new FastAPI backend. For actual legal advice, consult a lawyer."
    
    # Repealed Act Sentinel (PRD Loophole L-08)
    repealed_notice = ""
    if "ipc" in msg_lower or "indian penal code" in msg_lower:
        repealed_notice = "⚠️ NOTICE: The Indian Penal Code (IPC) has been repealed and replaced by the Bharatiya Nyaya Sanhita (BNS), 2023 effective July 1, 2024. Your references have been mapped to equivalent BNS provisions. "
    if "crpc" in msg_lower or "code of criminal procedure" in msg_lower:
        repealed_notice += "⚠️ NOTICE: The Code of Criminal Procedure (CrPC) has been repealed and replaced by the Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023. "
        
    # Entity Extraction
    # 1. Location
    cities = ["nagpur", "chennai", "delhi", "mumbai", "bengaluru", "kolkata", "pune", "hyderabad"]
    detected_city = None
    for city in cities:
        if city in msg_lower:
            detected_city = city.capitalize()
            break
            
    # 2. Monetary Values
    monetary_pattern = r"(?:rs\.?|inr|rupees)\s*\d+[\d,]*|\d+[\d,]*\s*(?:rs\.?|inr|rupees)"
    money_match = re.search(monetary_pattern, msg_lower)
    detected_amount = money_match.group(0).upper() if money_match else None
    
    # Intent / Category Classification
    if any(k in msg_lower for k in ["cheque", "bounced", "check bounce", "dishonour", "dishonor", "ni act"]):
        intent = "cheque_bounce"
        severity = "Criminal / Bailable"
        applicable_sections = ["Negotiable Instruments Act, 1881 (Section 138)"]
        next_steps = [
            "Send a written demand notice to the drawer within 30 days of receiving the cheque return memo from your bank.",
            "Give the drawer exactly 15 days from the receipt of the notice to make the payment.",
            "If they fail to pay within 15 days, file a formal criminal complaint under Section 138 in the Magistrate's court within 30 days of the cause of action."
        ]
        response = "Your query involves cheque bounce or dishonour of payments. Under Indian law, Section 138 of the Negotiable Instruments Act makes cheque bounce a criminal offence if the cheque was issued to discharge a legally enforceable debt."
        
    elif any(k in msg_lower for k in ["tenant", "landlord", "rent", "evict", "eviction", "lease", "owner", "deposit"]):
        intent = "tenancy"
        severity = "Civil Dispute"
        applicable_sections = ["Transfer of Property Act, 1882 (Section 106)", "State-Specific Rent Control Act"]
        next_steps = [
            "Review the terms of your registered Lease/Rent Agreement regarding eviction and notice periods.",
            "Serve a formal written legal notice to terminate the tenancy or demand return of security deposit (usually 15 days notice under Sec 106).",
            "If the dispute is unresolved, approach the local Rent Controller or Rent Authority in your jurisdiction."
        ]
        response = "Your query is related to landlord-tenant relations or eviction. Rental disputes in India are governed by the Transfer of Property Act, 1882, alongside state-specific Rent Control laws."

    elif any(k in msg_lower for k in ["consumer", "refund", "product", "defective", "warranty", "dealer", "service", "shop"]):
        intent = "consumer"
        severity = "Civil / Consumer Dispute"
        applicable_sections = ["Consumer Protection Act, 2019 (Section 35)"]
        next_steps = [
            "Send a formal written notice to the merchant/company outlining the product defect or deficiency in service and asking for redressal.",
            "If the company fails to respond, register a complaint online with the National Consumer Helpline (NCH).",
            "File an official complaint on the e-Daakhil portal to initiate proceedings before the District Consumer Commission."
        ]
        response = "Your query concerns consumer rights or deficient services. Under the Consumer Protection Act, 2019, consumers can seek compensation for defective goods, unfair trade practices, and subpar services."

    elif any(k in msg_lower for k in ["cyber", "online fraud", "hacked", "phishing", "scam", "defamation", "defame", "harassment", "post"]):
        intent = "cybercrime"
        severity = "Cognizable / Bailable"
        applicable_sections = ["Information Technology Act, 2000 (Section 66D)", "Bharatiya Nyaya Sanhita, 2023 (Section 356 - Defamation)"]
        next_steps = [
            "Take screenshots and preserve all URLs, emails, transaction IDs, or chat transcripts as digital evidence.",
            "Submit a formal complaint online at the National Cyber Crime Reporting Portal (cybercrime.gov.in) or visit your local Cyber Cell.",
            "For online financial fraud, contact your bank immediately to block accounts and request chargebacks."
        ]
        response = "Your query relates to cyber crimes, online fraud, or digital harassment. The Information Technology Act, 2000 (especially Section 66D for cheating by impersonation) and BNS govern these offenses."

    elif any(k in msg_lower for k in ["divorce", "marriage", "wife", "husband", "maintenance", "alimony", "custody", "family dispute"]):
        intent = "family"
        severity = "Civil / Family Dispute"
        applicable_sections = ["Hindu Marriage Act, 1955 (Section 13)", "Protection of Women from Domestic Violence Act, 2005"]
        next_steps = [
            "Attempt family mediation or counseling to explore amicable settlements.",
            "Draft a petition for mutual consent divorce under Section 13B of the HMA if both parties agree, or a contested petition if not.",
            "If needed, file a separate petition for interim maintenance or child custody under the relevant family laws."
        ]
        response = "Your query involves marital disputes, divorce, or alimony. Family matters in India are governed by personal laws (such as the Hindu Marriage Act, Special Marriage Act, or Muslim Personal Law) and civil procedures."

    elif any(k in msg_lower for k in ["assault", "police", "fir", "theft", "beaten", "robbery", "fraud", "criminal", "stole"]):
        intent = "criminal"
        severity = "Cognizable / Non-bailable"
        applicable_sections = ["Bharatiya Nyaya Sanhita, 2023 (Section 303/318)", "Bharatiya Nagarik Suraksha Sanhita, 2023 (Section 173)"]
        next_steps = [
            "Visit the nearest police station immediately to register a First Information Report (FIR) under Section 173 of the BNSS.",
            "Obtain a free copy of the registered FIR from the police officer.",
            "If the police refuse to register the FIR, file a written complaint to the Superintendent of Police (SP) or file a private complaint before the Magistrate."
        ]
        response = "Your query relates to a cognizable criminal offence. Under the new criminal codes (BNS and BNSS), registering a First Information Report (FIR) is the essential starting point for police investigation."

    else:
        intent = "general"
        severity = "Information Only"
        applicable_sections = ["Constitution of India", "Bharatiya Nyaya Sanhita, 2023"]
        next_steps = [
            "Prepare a chronological timeline of events with supporting documents (emails, letters, receipts).",
            "Identify if the dispute falls under civil remedies or criminal liabilities.",
            "Consult a specialized advocate to assess your legal standing."
        ]
        response = "Based on your description, I have analyzed the situation. This appears to involve standard constitutional challenges or statutory interpretation depending on the specific facts."

    # Append entity details to response
    context_notes = []
    if detected_city:
        context_notes.append(f"Jurisdiction context: {detected_city}")
    if detected_amount:
        context_notes.append(f"Financial claim value: {detected_amount}")
        
    if context_notes:
        response += " [Detected Context: " + ", ".join(context_notes) + "]"
        
    if repealed_notice:
        response = repealed_notice + response
        
    return {
        "response": response,
        "severity": severity,
        "applicableSections": applicable_sections,
        "nextSteps": next_steps,
        "disclaimer": disclaimer
    }

async def query_ollama(prompt: str) -> dict:
    url = f"{OLLAMA_HOST}/api/generate"
    system_prompt = (
        "You are Lex India, a source-backed legal assistant for Indian Law. "
        "Analyze the user query. Classify severity (e.g. 'Criminal / Bailable', 'Civil Dispute', 'Cognizable / Non-bailable'). "
        "Identify applicable acts and sections (e.g. 'Negotiable Instruments Act, 1881 (Section 138)'). "
        "List 2-3 practical next steps. "
        "Format your answer as a JSON object with these EXACT keys: "
        "'response' (a 2-3 sentence plain-language explanation), "
        "'severity' (the severity classification string), "
        "'applicableSections' (a JSON array of applicable sections/acts), "
        "'nextSteps' (a JSON array of next step strings). "
        "Do not include any Markdown wrapper like ```json or anything else. Output raw JSON only."
    )
    
    full_prompt = f"System: {system_prompt}\nUser: {prompt}\nJSON Output:"
    
    async with httpx.AsyncClient(timeout=8.0) as client:
        res = await client.post(
            url,
            json={"model": OLLAMA_MODEL, "prompt": full_prompt, "stream": False}
        )
        res.raise_for_status()
        res_json = res.json()
        raw_text = res_json.get("response", "").strip()
        
        # Clean potential markdown wrappers
        if raw_text.startswith("```"):
            raw_text = re.sub(r"^```(?:json)?\n|\n```$", "", raw_text, flags=re.M)
            
        data = json.loads(raw_text.strip())
        return {
            "response": data["response"],
            "severity": data["severity"],
            "applicableSections": data["applicableSections"],
            "nextSteps": data["nextSteps"],
            "disclaimer": "This is an AI-generated response from local Ollama. For actual legal advice, consult a lawyer."
        }

@router.post("/", response_model=ChatResponse)
async def chat_with_ai(
    request: ChatRequest,
    current_user: models.User = Depends(check_rate_limit)
):
    try:
        # Try Ollama connection
        try:
            analysis = await query_ollama(request.message)
        except Exception as e:
            # Fallback to local rule-based parser on connection refusal/invalid format
            analysis = analyze_message(request.message)
            analysis["disclaimer"] += " (Ollama offline; resolved via rule-based fallback)"
            
        return ChatResponse(
            response=analysis["response"],
            severity=analysis["severity"],
            applicableSections=analysis["applicableSections"],
            nextSteps=analysis["nextSteps"],
            disclaimer=analysis["disclaimer"]
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat processing error: {str(e)}")


