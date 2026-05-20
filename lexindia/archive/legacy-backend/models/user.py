from sqlalchemy import Column, Integer, String, DateTime
from db.postgres import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    bar_council_id = Column(String, nullable=True)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    query = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    compliance_status = Column(String)
