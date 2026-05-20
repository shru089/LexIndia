import json
import re
from typing import Dict

from services.llm_service import llm_service

class BriefGenerator:
    """
    MVP Feature 2: Structured AI Summarization.
    Transforms raw judgments into searchable, readable summaries.
    """
    
    async def generate_quick_summary(self, text: str) -> str:
        cleaned = " ".join(text.split())
        if not cleaned:
            return "No source text was provided for summarisation."

        if len(cleaned) < 320:
            return cleaned

        prompt = f"Summarize the following Indian court judgment in 3-5 lines, focusing on the core outcome:\n\n{text[:2000]}"
        if llm_service.can_attempt_generation():
            response = await llm_service.call_llama(prompt, system_prompt="You are a legal research assistant.")
            if not response.lower().startswith("error:"):
                return response

        sentences = re.split(r"(?<=[.!?])\s+", cleaned)
        return " ".join(sentences[:3])

    async def generate_detailed_summary(self, text: str) -> Dict:
        cleaned = " ".join(text.split())
        if not cleaned:
            return {
                "facts": "No text supplied.",
                "issue": "A source document is required.",
                "decision": "Unable to generate a brief without source text.",
                "reasoning": "Upload or paste a filing, judgment, or note to continue.",
            }

        prompt = (
            "Analyze the following judgment and provide a structured summary in JSON format with the fields: "
            "'facts', 'issue', 'decision', and 'reasoning'.\n\n"
            f"Judgment Text: {text[:4000]}"
        )
        if llm_service.can_attempt_generation():
            raw_response = await llm_service.call_llama(prompt, system_prompt="You are an expert legal analyst. Output ONLY JSON.")
            try:
                return json.loads(raw_response)
            except json.JSONDecodeError:
                pass

        sentences = re.split(r"(?<=[.!?])\s+", cleaned)
        return {
            "facts": " ".join(sentences[:2])[:320],
            "issue": "The primary legal or operational issue should be framed from the source material before external advice is issued.",
            "decision": "This deterministic fallback summary should be reviewed by counsel before circulation.",
            "reasoning": " ".join(sentences[2:5])[:420] if len(sentences) > 2 else cleaned[:420],
        }

brief_generator = BriefGenerator()
