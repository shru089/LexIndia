from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from db.postgres import get_db
from models.user import User
from services.auth.security import get_current_user
from services.demo_content import WORKFLOW_TEMPLATES
from services.workflow.citation_checker import validate_citation
from services.workflow.repository import create_workflow, list_workflows, update_workflow

router = APIRouter()


class CitationRequest(BaseModel):
    citation: str


class WorkflowCreateRequest(BaseModel):
    template_id: str | None = None
    name: str
    matter: str
    status: str = "intake"
    priority: str = "medium"
    summary: str | None = None
    next_action: str | None = None
    due_date: str | None = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class WorkflowUpdateRequest(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    summary: Optional[str] = None
    next_action: Optional[str] = None
    due_date: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@router.get("/")
async def get_workflow(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    all_records: bool = Query(False, description="Show every workflow instead of only the current user's"),
):
    owner_id = None if all_records and current_user.is_superuser else current_user.id
    return {
        "workflows": list_workflows(db, owner_id=owner_id),
        "templates": WORKFLOW_TEMPLATES,
        "status": "operational",
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_workflow_record(
    request: WorkflowCreateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create_workflow(
        db,
        {
            "owner_id": current_user.id,
            "template_id": request.template_id,
            "name": request.name,
            "matter": request.matter,
            "status": request.status,
            "priority": request.priority,
            "summary": request.summary,
            "next_action": request.next_action,
            "due_date": request.due_date,
            "metadata_json": request.metadata,
        },
    )


@router.patch("/{workflow_id}")
async def update_workflow_record(
    workflow_id: int,
    request: WorkflowUpdateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    existing_records = {item["id"]: item for item in list_workflows(db, owner_id=current_user.id)}
    if workflow_id not in existing_records and not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workflow not found.")

    payload: Dict[str, Any] = {}
    if request.status is not None:
        payload["status"] = request.status
    if request.priority is not None:
        payload["priority"] = request.priority
    if request.summary is not None:
        payload["summary"] = request.summary
    if request.next_action is not None:
        payload["next_action"] = request.next_action
    if request.due_date is not None:
        payload["due_date"] = request.due_date
    if request.metadata is not None:
        payload["metadata_json"] = request.metadata

    updated = update_workflow(db, workflow_id, payload)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workflow not found.")
    return updated


@router.post("/citation-check")
async def check_citation(request: CitationRequest):
    return await validate_citation(request.citation)
