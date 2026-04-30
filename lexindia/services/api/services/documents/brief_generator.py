from typing import Dict
from services.llm_service import llm_service
import json

class BriefGenerator:
    """
    MVP Feature 2: Structured AI Summarization.
    Transforms raw judgments into searchable, readable summaries.
    """
    
    async def generate_quick_summary(self, text: str) -> str:
        prompt = f"Summarize the following Indian court judgment in 3-5 lines, focusing on the core outcome:\n\n{text[:2000]}"
        return await llm_service.call_llama(prompt, system_prompt="You are a legal research assistant.")

    async def generate_detailed_summary(self, text: str) -> Dict:
        prompt = (
            "Analyze the following judgment and provide a structured summary in JSON format with the fields: "
            "'facts', 'issue', 'decision', and 'reasoning'.\n\n"
            f"Judgment Text: {text[:4000]}"
        )
        raw_response = await llm_service.call_llama(prompt, system_prompt="You are an expert legal analyst. Output ONLY JSON.")
        
        try:
            return json.loads(raw_response)
        except:
            return {"error": "Failed to parse AI summary", "raw": raw_response[:200]}

brief_generator = BriefGenerator()
