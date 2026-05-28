from fastapi import APIRouter
from pydantic import BaseModel

from services.demo_content import DOCUMENT_CAPABILITIES
from services.documents.brief_generator import brief_generator
from services.documents.comparator import comparator
from services.documents.ocr import run_ocr

router = APIRouter()


class CompareRequest(BaseModel):
    document_a: str
    document_b: str


class BriefRequest(BaseModel):
    text: str


class OcrRequest(BaseModel):
    file_path: str = "demo-scan.pdf"


@router.get("/")
async def get_docs():
    return {
        "module": "documents",
        "capabilities": DOCUMENT_CAPABILITIES,
        "status": "operational",
    }


@router.post("/brief")
async def create_brief(request: BriefRequest):
    quick_summary = await brief_generator.generate_quick_summary(request.text)
    detailed_summary = await brief_generator.generate_detailed_summary(request.text)
    return {
        "quick_summary": quick_summary,
        "detailed_summary": detailed_summary,
    }


@router.post("/compare")
async def compare_documents(request: CompareRequest):
    contradictions = await comparator.find_contradictions(request.document_a, request.document_b)
    return {
        "contradictions": contradictions,
        "document_a_length": len(request.document_a),
        "document_b_length": len(request.document_b),
    }


@router.post("/ocr")
async def extract_document_text(request: OcrRequest):
    extracted_text = await run_ocr(request.file_path)
    return {"file_path": request.file_path, "text": extracted_text}
