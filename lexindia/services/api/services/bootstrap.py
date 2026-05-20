from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from config import settings
from db.postgres import create_all_tables, get_session_factory
from models.judgment import Judgment
from models.section import LegalSection
from models.user import User
from models.workflow import WorkflowRecord
from services.demo_content import LEGAL_CORPUS, SECTION_MAP, WORKFLOW_TEMPLATES
from services.auth.security import hash_password


def _seed_sections(db: Session) -> None:
    existing = db.execute(select(LegalSection.id).limit(1)).scalar_one_or_none()
    if existing is not None:
        return

    for section_number, payload in SECTION_MAP.items():
        db.add(
            LegalSection(
                act_name="BNS",
                section_number=payload["bns_section"],
                title=payload["title"],
                content=payload["description"],
                notes=f"Mapped from {payload['legacy_section']}",
            )
        )
        db.add(
            LegalSection(
                act_name="IPC",
                section_number=section_number,
                title=payload["title"],
                content=payload["description"],
                notes=f"Mapped to BNS {payload['bns_section']}",
            )
        )


def _seed_judgments(db: Session) -> None:
    existing = db.execute(select(Judgment.id).limit(1)).scalar_one_or_none()
    if existing is not None:
        return

    for entry in LEGAL_CORPUS:
        if entry["source"] not in {"judgment", "playbook", "statute"}:
            continue

        db.add(
            Judgment(
                title=entry["title"],
                case_number=entry.get("citation"),
                court_name=entry.get("court"),
                content=entry.get("content"),
                summary=entry.get("summary"),
                metadata_json={"topic": entry.get("topic"), "keywords": entry.get("keywords", [])},
                citations=entry.get("recommended_actions", []),
            )
        )


def _seed_admin_user(db: Session) -> None:
    if not settings.BOOTSTRAP_ADMIN_EMAIL or not settings.BOOTSTRAP_ADMIN_PASSWORD:
        return

    admin_email = settings.BOOTSTRAP_ADMIN_EMAIL.strip().lower()
    existing = db.execute(select(User).where(User.email == admin_email)).scalar_one_or_none()
    if existing is not None:
        return

    db.add(
        User(
            email=admin_email,
            full_name=settings.BOOTSTRAP_ADMIN_NAME,
            hashed_password=hash_password(settings.BOOTSTRAP_ADMIN_PASSWORD),
            role="admin",
            is_active=True,
            is_superuser=True,
            is_verified=True,
            auth_provider="lexindia",
        )
    )


def _seed_workflows(db: Session) -> None:
    existing = db.execute(select(WorkflowRecord.id).limit(1)).scalar_one_or_none()
    if existing is not None:
        return

    for template in WORKFLOW_TEMPLATES:
        db.add(
            WorkflowRecord(
                owner_id=None,
                template_id=template["id"],
                name=template["name"],
                matter=f"{template['name']} pilot setup",
                status=template["stage"].lower(),
                priority="medium",
                summary=template["summary"],
                next_action="Review pilot readiness and assign an owner.",
                due_date=None,
                metadata_json={"sla": template["sla"], "seeded": True},
            )
        )


def initialize_persistence(seed_demo_data: bool = False) -> None:
    create_all_tables()
    session = get_session_factory()()
    try:
        if seed_demo_data:
            _seed_sections(session)
            _seed_judgments(session)
            _seed_workflows(session)

        if settings.BOOTSTRAP_MODE:
            _seed_admin_user(session)

        session.commit()
    finally:
        session.close()
