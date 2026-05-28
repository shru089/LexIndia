from __future__ import annotations

from typing import Any, Dict, List

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.workflow import WorkflowRecord


def serialize_workflow(record: WorkflowRecord) -> Dict[str, Any]:
    return {
        "id": record.id,
        "template_id": record.template_id,
        "name": record.name,
        "matter": record.matter,
        "status": record.status,
        "priority": record.priority,
        "summary": record.summary,
        "next_action": record.next_action,
        "due_date": record.due_date,
        "metadata": record.metadata_json or {},
        "owner_id": record.owner_id,
        "created_at": record.created_at.isoformat() if record.created_at else None,
        "updated_at": record.updated_at.isoformat() if record.updated_at else None,
    }


def list_workflows(db: Session, owner_id: int | None = None) -> List[Dict[str, Any]]:
    statement = select(WorkflowRecord).order_by(WorkflowRecord.updated_at.desc())
    if owner_id is not None:
        statement = statement.where(WorkflowRecord.owner_id == owner_id)
    records = db.execute(statement).scalars().all()
    return [serialize_workflow(record) for record in records]


def create_workflow(db: Session, payload: Dict[str, Any]) -> Dict[str, Any]:
    record = WorkflowRecord(**payload)
    db.add(record)
    db.commit()
    db.refresh(record)
    return serialize_workflow(record)


def update_workflow(db: Session, workflow_id: int, payload: Dict[str, Any]) -> Dict[str, Any] | None:
    record = db.get(WorkflowRecord, workflow_id)
    if record is None:
        return None

    for key, value in payload.items():
        setattr(record, key, value)

    db.add(record)
    db.commit()
    db.refresh(record)
    return serialize_workflow(record)
