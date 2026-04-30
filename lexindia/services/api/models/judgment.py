from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from db.postgres import Base

class Judgment(Base):
    __tablename__ = "judgments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    case_number = Column(String, index=True)
    court_name = Column(String, index=True)
    judge_names = Column(JSON) # List of judges
    judgment_date = Column(DateTime)
    content = Column(Text)
    summary = Column(Text)
    metadata_json = Column(JSON) # Catch-all for extra info
    citations = Column(JSON) # List of other cases cited
    created_at = Column(DateTime(timezone=True), server_default=func.now())
