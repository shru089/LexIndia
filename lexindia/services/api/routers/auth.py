from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from config import settings

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(request: LoginRequest):
    if not settings.ALLOW_DEMO_AUTH:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Authentication is not configured yet",
        )

    if request.email == "test@nyaya.ai" and request.password == "password":
        return {"access_token": "placeholder_token", "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
    )

@router.post("/verify-bar-council")
async def verify_bar_council(id: str):
    if not settings.ALLOW_DEMO_AUTH:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Bar council verification is not configured yet",
        )

    return {"verified": True, "id": id}
