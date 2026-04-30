"""
Audit Logger: Implements immutable logging for legal compliance.
"""
from datetime import datetime
from db.postgres import SessionLocal
from models.query import AuditLog

async def log_interaction(user_id: int, query: str, response: str, intent: str, sources: list):
    """
    Logs every query and response to the PostgreSQL database for a 2-year retention period.
    """
    db = SessionLocal()
    try:
        log_entry = AuditLog(
            user_id=user_id,
            query_text=query,
            ai_response=response,
            sources_cited=sources,
            intent=intent,
            is_safe=1
        )
        db.add(log_entry)
        db.commit()
    finally:
        db.close()
