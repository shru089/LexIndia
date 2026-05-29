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
    case_number: Optional[str] = None
    bench: Optional[str] = None
    date: Optional[str] = None
    acts_cited: Optional[str] = None
    sections_cited: Optional[str] = None
    outcome: Optional[str] = None
    key_parties: Optional[str] = None
    summary_facts: Optional[str] = None
    summary_held: Optional[str] = None
    summary_ratio: Optional[str] = None
    amended_recently: bool

class CasesResponse(BaseModel):
    results: List[CaseResponse]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=CasesResponse)
def get_cases(
    q: Optional[str] = None,
    court: Optional[str] = None,
    year: Optional[int] = None,
    outcome: Optional[str] = None,
    act: Optional[str] = None,
    amended_recently: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    try:
        query = db.query(models.Case)
        if q:
            # Search across title, key_parties, or acts_cited
            query = query.filter(
                (models.Case.title.ilike(f"%{q}%")) |
                (models.Case.key_parties.ilike(f"%{q}%")) |
                (models.Case.acts_cited.ilike(f"%{q}%"))
            )
        if court:
            query = query.filter(models.Case.court.ilike(f"%{court}%"))
        if year is not None:
            query = query.filter(models.Case.year == year)
        if outcome:
            query = query.filter(models.Case.outcome.ilike(f"%{outcome}%"))
        if act:
            query = query.filter(models.Case.acts_cited.ilike(f"%{act}%"))
        if amended_recently is not None:
            query = query.filter(models.Case.amended_recently == amended_recently)

        cases = query.all()

        results = [
            {
                "id": str(c.id),
                "title": c.title,
                "year": c.year,
                "court": c.court,
                "citation": c.citation,
                "case_number": c.case_number,
                "bench": c.bench,
                "date": c.date,
                "acts_cited": c.acts_cited,
                "sections_cited": c.sections_cited,
                "outcome": c.outcome,
                "key_parties": c.key_parties,
                "summary_facts": c.summary_facts,
                "summary_held": c.summary_held,
                "summary_ratio": c.summary_ratio,
                "amended_recently": c.amended_recently
            } for c in cases
        ]
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

