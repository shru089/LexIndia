from sqlalchemy import Column, Integer, String, Text, Boolean
from database import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    court = Column(String)
    citation = Column(String)
    case_number = Column(String, index=True, nullable=True)
    bench = Column(String, nullable=True)
    date = Column(String, nullable=True)
    acts_cited = Column(String, nullable=True)  # Comma-separated list of acts
    sections_cited = Column(String, nullable=True)  # Comma-separated list of sections
    outcome = Column(String, index=True, nullable=True)
    key_parties = Column(String, nullable=True)
    summary_facts = Column(Text, nullable=True)
    summary_held = Column(Text, nullable=True)
    summary_ratio = Column(Text, nullable=True)
    amended_recently = Column(Boolean, default=False)
    full_text = Column(Text, nullable=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    tier = Column(String, default="free", nullable=False)  # 'free', 'citizen_pro', 'advocate'


