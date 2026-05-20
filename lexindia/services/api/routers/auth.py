from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.postgres import get_active_database_url, get_db
from models.user import User
from services.auth.security import create_access_token, get_current_user, hash_password, verify_password

router = APIRouter()


class RegisterRequest(BaseModel):
    email: str
    password: str = Field(min_length=8)
    full_name: str
    role: str = "counsel"
    bar_council_id: str | None = None


class LoginRequest(BaseModel):
    email: str
    password: str


class VerifyBarCouncilRequest(BaseModel):
    bar_council_id: str = Field(min_length=4)


@router.get("/status")
async def auth_status():
    active_database = get_active_database_url()
    return {
        "configured": True,
        "mode": "jwt",
        "provider": "lexindia-local-idp",
        "database": active_database,
        "message": "LexIndia identity is active with JWT access tokens and persistent local accounts.",
    }


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    normalized_email = request.email.strip().lower()
    if "@" not in normalized_email:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="A valid email address is required.")

    existing_user = db.execute(select(User).where(User.email == normalized_email)).scalar_one_or_none()
    if existing_user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="A user with this email already exists.")

    if request.bar_council_id:
        duplicate_bar_id = db.execute(
            select(User).where(User.bar_council_id == request.bar_council_id)
        ).scalar_one_or_none()
        if duplicate_bar_id is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This bar council ID is already in use.")

    user = User(
        email=normalized_email,
        full_name=request.full_name,
        hashed_password=hash_password(request.password),
        role=request.role,
        bar_council_id=request.bar_council_id,
        is_verified=bool(request.bar_council_id),
        auth_provider="lexindia",
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(subject=user.email, extra_claims={"user_id": user.id, "role": user.role})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role,
            "is_verified": user.is_verified,
        },
    }


@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    normalized_email = request.email.strip().lower()
    user = db.execute(select(User).where(User.email == normalized_email)).scalar_one_or_none()
    if user is None or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password.")

    token = create_access_token(subject=user.email, extra_claims={"user_id": user.id, "role": user.role})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role,
            "is_verified": user.is_verified,
        },
    }


@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "full_name": current_user.full_name,
        "role": current_user.role,
        "bar_council_id": current_user.bar_council_id,
        "is_verified": current_user.is_verified,
    }


@router.post("/verify-bar-council")
async def verify_bar_council(
    request: VerifyBarCouncilRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    current_user.bar_council_id = request.bar_council_id
    current_user.is_verified = True
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return {"verified": True, "bar_council_id": current_user.bar_council_id}
