from typing import List, Dict, Optional
from pydantic import BaseModel

class NyayaResponse(BaseModel):
    situation_summary: str
    applicable_laws: List[Dict[str, str]] # Act -> Section -> Explanation
    similar_case_insights: Dict[str, any]
    next_steps: List[str]
    confidence_level: str # High / Moderate / Low
    sources: List[str]
    disclaimer: str = "This is legal information, not legal advice. Please consult a licensed advocate before taking action."

from services.llm_service import llm_service

SYSTEM_PROMPT = """
You are Nyaya.AI — an AI-powered legal intelligence system built for India.
Provide legal information, NOT legal advice. Use suggestive language: 'may apply', 'in similar cases...', 'you may consider...'.
... (Rest of the mandatory system prompt logic) ...
"""

class ResponseGenerator:
    async def generate_structured_response(self, query: str, context: List[Dict]) -> NyayaResponse:
        # Construct the prompt with retrieved context
        context_str = "\n".join([str(c) for c in context])
        prompt = f"User Query: {query}\n\nRetrieved Legal Context:\n{context_str}\n\nPlease provide a structured response according to the Nyaya.AI mandatory format."
        
        # Call the real Llama 3
        raw_response = await llm_service.call_llama(prompt, system_prompt=SYSTEM_PROMPT)
        
        # In a real scenario, we'd parse the LLM output into the Pydantic model
        # For now, we return the model with the LLM's raw output mapped to fields
        return NyayaResponse(
            situation_summary=raw_response[:200], # Simplified mapping
            applicable_laws=[],
            similar_case_insights={},
            next_steps=["Please review the analysis provided by Llama 3."],
            confidence_level="High",
            sources=["Retrieved from Database"]
        )

generator = ResponseGenerator()
