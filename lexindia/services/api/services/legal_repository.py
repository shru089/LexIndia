from __future__ import annotations

from typing import Any, Dict, List

from sqlalchemy import or_, select
from sqlalchemy.exc import SQLAlchemyError

from db.postgres import get_session_factory
from models.judgment import Judgment
from models.section import LegalSection


def search_live_legal_data(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    session = get_session_factory()()
    try:
        like_query = f"%{query}%"

        judgments = session.execute(
            select(Judgment)
            .where(
                or_(
                    Judgment.title.ilike(like_query),
                    Judgment.content.ilike(like_query),
                    Judgment.summary.ilike(like_query),
                    Judgment.case_number.ilike(like_query),
                )
            )
            .limit(limit)
        ).scalars().all()

        sections = session.execute(
            select(LegalSection)
            .where(
                or_(
                    LegalSection.act_name.ilike(like_query),
                    LegalSection.section_number.ilike(like_query),
                    LegalSection.title.ilike(like_query),
                    LegalSection.content.ilike(like_query),
                    LegalSection.notes.ilike(like_query),
                )
            )
            .limit(limit)
        ).scalars().all()

        results: List[Dict[str, Any]] = []
        for judgment in judgments:
            results.append(
                {
                    "id": f"judgment-{judgment.id}",
                    "title": judgment.title,
                    "summary": judgment.summary or (judgment.content or "")[:280],
                    "citation": judgment.case_number,
                    "source": "judgment-db",
                    "topic": "Case law",
                    "court": judgment.court_name,
                    "recommended_actions": [
                        "Validate the case ratio and current applicability before reliance.",
                    ],
                    "score": 90.0,
                }
            )

        for section in sections:
            results.append(
                {
                    "id": f"section-{section.id}",
                    "title": f"{section.act_name} Section {section.section_number}: {section.title}",
                    "summary": section.notes or (section.content or "")[:280],
                    "citation": f"{section.act_name} {section.section_number}",
                    "source": "section-db",
                    "topic": "Statutory law",
                    "court": "Legislative",
                    "recommended_actions": [
                        "Check whether later amendments or successor codes affect this provision.",
                    ],
                    "score": 88.0,
                }
            )

        return results[:limit]
    except SQLAlchemyError:
        return []
    finally:
        session.close()
