from __future__ import annotations

from pathlib import Path
from typing import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import settings


class Base(DeclarativeBase):
    pass


_engine: Engine | None = None
_session_factory: sessionmaker[Session] | None = None
_active_database_url: str | None = None


def reset_database_state() -> None:
    global _engine, _session_factory, _active_database_url
    if _engine is not None:
        _engine.dispose()
    _engine = None
    _session_factory = None
    _active_database_url = None


def _normalise_sqlite_url(url: str) -> str:
    if url.startswith("sqlite:///"):
        return url

    db_path = Path(url).resolve()
    return f"sqlite:///{db_path.as_posix()}"


def _build_engine(url: str) -> Engine:
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, pool_pre_ping=True, future=True, connect_args=connect_args)


def _ensure_engine() -> None:
    global _engine, _session_factory, _active_database_url
    if _engine is not None and _session_factory is not None:
        return

    primary_url = settings.DATABASE_URL
    fallback_url = _normalise_sqlite_url(settings.DATABASE_FALLBACK_URL)

    try:
        engine = _build_engine(primary_url)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        _engine = engine
        _active_database_url = primary_url
    except SQLAlchemyError:
        if not settings.ENABLE_DB_FALLBACK or not (settings.is_dev or settings.is_test):
            raise
        engine = _build_engine(fallback_url)
        _engine = engine
        _active_database_url = fallback_url

    _session_factory = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=_engine,
        expire_on_commit=False,
    )


def get_engine() -> Engine:
    _ensure_engine()
    assert _engine is not None
    return _engine


def get_session_factory() -> sessionmaker[Session]:
    _ensure_engine()
    assert _session_factory is not None
    return _session_factory


def get_active_database_url() -> str:
    _ensure_engine()
    return _active_database_url or settings.DATABASE_URL


def create_all_tables() -> None:
    engine = get_engine()
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    session = get_session_factory()()
    try:
        yield session
    finally:
        session.close()
