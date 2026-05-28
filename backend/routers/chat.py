from fastapi import APIRouter
from pydantic import BaseModel
import asyncio

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat_with_ai(request: ChatRequest):
    await asyncio.sleep(1.5)
    
    return {
        "response": f"Based on your description: '{request.message}', I have analyzed the situation. This appears to involve standard constitutional challenges or statutory interpretation depending on the specific facts.",
        "severity": "Information Only",
        "applicableSections": ["Const. Art 32", "Const. Art 226"],
        "nextSteps": [
            "Consult a specialized advocate.",
            "Review recent High Court precedents on similar matters."
        ],
        "disclaimer": "This is a simulated AI response from the new FastAPI backend. For actual legal advice, consult a lawyer."
    }
