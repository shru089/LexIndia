from fastapi import APIRouter, HTTPException, Query
from services.rag.retriever import retriever

router = APIRouter()


@router.get("/search")
async def search_legal(
    query: str = Query(..., min_length=1, description="Legal search query"),
    limit: int = Query(10, ge=1, le=50, description="Max number of results"),
):
    """
    Perform hybrid search across judgments and statutes.
    Returns ranked results via Reciprocal Rank Fusion (RRF).
    """
    results = await retriever.retrieve(query, limit=limit)
    return {"query": query, "count": len(results), "results": results}


@router.post("/analyze")
async def analyze_legal_scenario(scenario: str = Query(..., min_length=1)):
    """
    Analyze a legal scenario using RAG and LLM.
    """
    # TODO: wire to generator service once LLM is configured
    return {"analysis": "Scenario analysis in progress...", "scenario": scenario}


@router.get("/health")
async def research_health():
    """Quick liveness check for the research module."""
    return {"status": "ok", "module": "research"}
