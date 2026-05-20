from typing import Any, Dict, List

from pydantic import BaseModel


class NyayaResponse(BaseModel):
    situation_summary: str
    applicable_laws: List[Dict[str, str]]
    similar_case_insights: Dict[str, Any]
    next_steps: List[str]
    confidence_level: str
    sources: List[str]
    disclaimer: str = "This is legal information, not legal advice. Please consult a licensed advocate before taking action."


class ResponseGenerator:
    async def generate_structured_response(self, query: str, context: List[Dict[str, Any]]) -> NyayaResponse:
        sources = [item["title"] for item in context[:3]]
        applicable_laws = []
        for item in context[:3]:
            applicable_laws.append(
                {
                    "title": item.get("title", "Authority"),
                    "source": item.get("source", "research"),
                    "citation": item.get("citation", "Internal demo brief"),
                }
            )

        return NyayaResponse(
            situation_summary=f"LexIndia identified the request as: {query}. The strongest immediate posture is to organise facts, authorities, and the next operational checkpoint before drafting advice or submissions.",
            applicable_laws=applicable_laws,
            similar_case_insights={
                "context_count": len(context),
                "priority_theme": context[0].get("topic", "General legal research") if context else "General legal research",
            },
            next_steps=[
                "Validate the fact pattern against the most relevant authority.",
                "Create a short note distinguishing what is known from what still needs verification.",
                "Escalate to a licensed advocate before final legal advice or filing action.",
            ],
            confidence_level="Moderate" if context else "Low",
            sources=sources or ["LexIndia demo corpus"],
        )


generator = ResponseGenerator()
