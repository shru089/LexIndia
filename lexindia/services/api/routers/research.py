from fastapi import APIRouter, HTTPException
from services.rag.retriever import retriever

router = APIRouter()

@router.get("/search")
async def search_legal(query: str):
    """
    Perform hybrid search across judgments and statutes.
    """
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    results = await retriever.retrieve(query)
    return {"query": query, "count": len(results), "results": results}

@router.post("/analyze")
async def analyze_legal_scenario(scenario: str):
    """
    Analyze a legal scenario using RAG and LLM.
    """
    # This would call the generator service
    return {"analysis": "Scenario analysis in progress...", "scenario": scenario}
