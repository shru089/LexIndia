from sqlalchemy import Column, Integer, String, Text, ForeignKey
from db.postgres import Base

class LegalSection(Base):
    __tablename__ = "statutes"

    id = Column(Integer, primary_key=True, index=True)
    act_name = Column(String, index=True) # e.g., IPC, BNS
    section_number = Column(String, index=True)
    title = Column(String)
    content = Column(Text)
    mapped_section_id = Column(Integer, ForeignKey("statutes.id"), nullable=True)
    notes = Column(String, nullable=True)
