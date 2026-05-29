from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    severity: str
    applicableSections: list
    nextSteps: list
    disclaimer: str

@router.post("/", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    try:
        if not request.message or not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        await asyncio.sleep(1.5)
        
        return ChatResponse(
            response=f"Based on your description: '{request.message}', I have analyzed the situation. This appears to involve standard constitutional challenges or statutory interpretation depending on the specific facts.",
            severity="Information Only",
            applicableSections=["Const. Art 32", "Const. Art 226"],
            nextSteps=[
                "Consult a specialized advocate.",
                "Review recent High Court precedents on similar matters."
            ],
            disclaimer="This is a simulated AI response from the new FastAPI backend. For actual legal advice, consult a lawyer."
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat processing error: {str(e)}")
