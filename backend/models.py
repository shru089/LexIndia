from sqlalchemy import Column, Integer, String, Text
from database import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    court = Column(String)
    citation = Column(String)
    full_text = Column(Text, nullable=True)
