from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from db.postgres import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    query_text = Column(Text)
    ai_response = Column(Text)
    sources_cited = Column(JSON)
    intent = Column(String) # e.g., "info", "advice"
    is_safe = Column(Integer) # 1 for safe, 0 for blocked
    created_at = Column(DateTime(timezone=True), server_default=func.now())
