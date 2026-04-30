from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from db.supabase_client import supabase

router = APIRouter()

class AuthRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
async def register(request: AuthRequest):
    """
    Registers a new user in Supabase.
    """
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
        
    response = supabase.auth.sign_up({
        "email": request.email,
        "password": request.password
    })
    
    if response.user:
        return {"message": "User registered successfully", "user_id": response.user.id}
    else:
        raise HTTPException(status_code=400, detail="Registration failed")

@router.post("/login")
async def login(request: AuthRequest):
    """
    Logs in a user and returns a Supabase session.
    """
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
        
    try:
        response = supabase.auth.sign_in_with_password({
            "email": request.email,
            "password": request.password
        })
        return {
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token,
            "user": response.user
        }
from services.bar_council import bc_verifier

class BarCouncilRequest(BaseModel):
    enrollment_no: str
    state: str

@router.post("/verify-bar-council")
async def verify_bar_council(request: BarCouncilRequest):
    """
    Verifies an advocate's Bar Council ID.
    """
    result = await bc_verifier.verify_advocate(request.enrollment_no, request.state)
    if result["verified"]:
        return result
    else:
        raise HTTPException(status_code=400, detail=result["message"])
