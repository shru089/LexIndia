from fastapi import APIRouter, Query

from services.demo_content import section_matches

router = APIRouter()


@router.get("/")
async def get_navigate(query: str = Query("", description="Optional section or topic to translate")):
    matches = section_matches(query) if query else []
    return {
        "status": "operational",
        "query": query,
        "matches": matches,
        "guidance": "Use this route to translate IPC references into their BNS equivalents during legal research and drafting.",
    }
