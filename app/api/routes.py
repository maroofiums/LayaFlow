from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.container import (
    decision_engine,
    workflow_orchestrator,
)
from app.database.database import get_db
from app.database.repository import (
    create_request,
    get_request,
    get_requests,
    update_request_decision,
)
from app.decisions.schemas import SupportRequest


router = APIRouter(
    prefix="/api",
    tags=["requests"],
)


@router.post("/requests/process")
def process_request(
    request: SupportRequest,
    db: Session = Depends(get_db),
):
    db_request = create_request(
        db=db,
        title=request.title,
        description=request.description,
    )

    decision = decision_engine.decide(request)

    workflow = workflow_orchestrator.execute(decision)

    update_request_decision(
        db=db,
        request=db_request,
        category=decision.category.value,
        priority=decision.priority.value,
        escalation_probability=decision.escalation_probability,
        workflow_status=workflow.status.value,
        assigned_team=workflow.assigned_team,
        workflow_action=workflow.action,
    )

    return {
        "id": db_request.id,
        "request": request,
        "decision": decision,
        "workflow": workflow,
    }


@router.get("/requests")
def list_requests(
    db: Session = Depends(get_db),
):
    return get_requests(db)


@router.get("/requests/{request_id}")
def retrieve_request(
    request_id: int,
    db: Session = Depends(get_db),
):
    request = get_request(db, request_id)

    if request is None:
        raise HTTPException(
            status_code=404,
            detail="Request not found",
        )

    return request