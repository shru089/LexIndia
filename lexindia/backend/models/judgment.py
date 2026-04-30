from sqlalchemy import Column, Integer, String, Text, Date
from db.postgres import Base

class Judgment(Base):
    __tablename__ = "judgments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    case_id = Column(String, unique=True, index=True)
    full_text = Column(Text)
    court = Column(String, index=True)
    date_published = Column(Date)
