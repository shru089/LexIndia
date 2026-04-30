from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.draft_engine import drafting_engine

router = APIRouter()

class DocumentRequest(BaseModel):
    template_name: str
    data: dict

@router.post("/generate")
async def generate_legal_document(request: DocumentRequest):
    """
    Generates a legal document based on a template (fir_draft, affidavit, etc.)
    """
    try:
        content = await drafting_engine.generate_document(request.template_name, request.data)
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
