from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from typing import Optional, List
from pydantic import BaseModel

router = APIRouter()

class CaseResponse(BaseModel):
    id: str
    title: str
    year: int
    court: str
    citation: str

class CasesResponse(BaseModel):
    results: List[CaseResponse]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=CasesResponse)
def get_cases(q: Optional[str] = None, db: Session = Depends(get_db)):
    try:
        query = db.query(models.Case)
        if q:
            query = query.filter(models.Case.title.ilike(f"%{q}%"))
        cases = query.all()
        
        results = [
            {
                "id": str(c.id),
                "title": c.title,
                "year": c.year,
                "court": c.court,
                "citation": c.citation
            } for c in cases
        ]
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
