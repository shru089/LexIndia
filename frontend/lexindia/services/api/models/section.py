from sqlalchemy import Column, Integer, String, Text
from db.postgres import Base

class LegalSection(Base):
    __tablename__ = "legal_sections"

    id = Column(Integer, primary_key=True, index=True)
    act_name = Column(String, index=True) # e.g., "IPC", "BNS"
    section_number = Column(String, index=True)
    title = Column(String)
    content = Column(Text)
    mapped_section_id = Column(Integer) # ID of corresponding section in other act
    notes = Column(Text)
