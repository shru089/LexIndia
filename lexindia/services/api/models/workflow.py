from sqlalchemy import Column, DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.sql import func

from db.postgres import Base


class WorkflowRecord(Base):
    __tablename__ = "workflow_records"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    template_id = Column(String, index=True)
    name = Column(String, nullable=False)
    matter = Column(String, nullable=False)
    status = Column(String, default="intake", index=True)
    priority = Column(String, default="medium", index=True)
    summary = Column(Text)
    next_action = Column(Text)
    due_date = Column(String)
    metadata_json = Column(JSON, default=dict)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
