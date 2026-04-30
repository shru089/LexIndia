"""
Section Identifier (Legal GPS): Maps plain language problems to specific Acts and Sections.
"""
from typing import List, Dict

from services.llm_service import llm_service
import json

class LegalGPS:
    async def identify_sections(self, problem_description: str) -> List[Dict]:
        prompt = (
            "Given the following legal problem description in India, identify the most relevant Acts and Sections. "
            "Include BNS (Bharatiya Nyaya Sanhita) if applicable. Output a JSON list of objects with "
            "'act', 'section', 'title', 'meaning', and 'remedy'.\n\n"
            f"Problem: {problem_description}"
        )
        raw_response = await llm_service.call_llama(prompt, system_prompt="You are a legal navigation expert. Output ONLY JSON.")
        
        try:
            return json.loads(raw_response)
        except:
            return []

legal_gps = LegalGPS()

legal_gps = LegalGPS()
