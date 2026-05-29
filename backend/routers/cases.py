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

class PaginationMetadata(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int
    has_next: bool
    has_prev: bool

class CasesResponse(BaseModel):
    results: List[CaseResponse]
    pagination: PaginationMetadata

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
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):
    try:
        # Enforce minimum bounds
        if page < 1:
            page = 1
        if page_size < 1:
            page_size = 10

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

        # Count total matches before pagination limit
        total_count = query.count()

        # Apply offset and limit
        offset = (page - 1) * page_size
        cases = query.offset(offset).limit(page_size).all()

        import math
        total_pages = math.ceil(total_count / page_size) if total_count > 0 else 0
        has_next = page < total_pages
        has_prev = page > 1

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
        
        return {
            "results": results,
            "pagination": {
                "total": total_count,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages,
                "has_next": has_next,
                "has_prev": has_prev
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


