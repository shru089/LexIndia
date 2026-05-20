from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db.postgres import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String)
    hashed_password = Column(String)
    role = Column(String, default="counsel")
    auth_provider = Column(String, default="lexindia")
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    bar_council_id = Column(String, unique=True, index=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
