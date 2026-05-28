from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from typing import Optional

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_cases(q: Optional[str] = None, db: Session = Depends(get_db)):
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
