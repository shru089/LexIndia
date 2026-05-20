from typing import Optional

from fastapi import APIRouter, Query
from pydantic import BaseModel

from services.demo_content import build_analysis, get_briefing_payload
from services.rag.generator import generator
from services.rag.retriever import retriever

router = APIRouter()


class AnalyzeRequest(BaseModel):
    scenario: str


@router.get("/search")
async def search_legal(
    query: str = Query(..., min_length=1, description="Legal search query"),
    limit: int = Query(10, ge=1, le=50, description="Max number of results"),
):
    results = await retriever.retrieve(query, limit=limit)
    return {
        "query": query,
        "count": len(results),
        "results": results,
        "meta": {
            "mode": "hybrid-with-demo-fallback",
            "advisory": "Results support legal research workflows and should be validated before filing or formal advice.",
        },
    }


@router.post("/analyze")
async def analyze_legal_scenario(
    payload: Optional[AnalyzeRequest] = None,
    scenario: Optional[str] = Query(None, min_length=1),
):
    final_scenario = (payload.scenario if payload else scenario) or ""
    context = await retriever.retrieve(final_scenario, limit=5)
    response = await generator.generate_structured_response(final_scenario, context)
    return {
        "scenario": final_scenario,
        "analysis": build_analysis(final_scenario, context),
        "structured_response": response.model_dump(),
    }


@router.get("/briefing")
async def research_briefing():
    return get_briefing_payload()


@router.get("/health")
async def research_health():
    return {"status": "ok", "module": "research"}
