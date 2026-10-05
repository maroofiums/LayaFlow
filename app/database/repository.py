from sqlalchemy.orm import Session

from app.database.models import RequestRecord, WorkflowEvent


def create_request(
    db: Session,
    title: str,
    description: str,
) -> RequestRecord:

    request = RequestRecord(
        title=title,
        description=description,
    )

    db.add(request)
    db.commit()
    db.refresh(request)

    return request


def get_request(
    db: Session,
    request_id: int,
) -> RequestRecord | None:

    return db.get(RequestRecord, request_id)


def get_requests(
    db: Session,
) -> list[RequestRecord]:

    return (
        db.query(RequestRecord)
        .order_by(RequestRecord.created_at.desc())
        .all()
    )


def update_request_decision(
    db: Session,
    request: RequestRecord,
    category: str,
    priority: str,
    escalation_probability: float,
    workflow_status: str,
    assigned_team: str,
    workflow_action: str,
) -> RequestRecord:

    request.category = category
    request.priority = priority
    request.escalation_probability = escalation_probability
    request.workflow_status = workflow_status
    request.assigned_team = assigned_team
    request.workflow_action = workflow_action

    db.commit()
    db.refresh(request)

    return request



def create_event(
    db: Session,
    request_id: int,
    event_type: str,
    description: str | None = None,
) -> WorkflowEvent:

    event = WorkflowEvent(
        request_id=request_id,
        event_type=event_type,
        description=description,
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event



def get_request_events(
    db: Session,
    request_id: int,
) -> list[WorkflowEvent]:

    return (
        db.query(WorkflowEvent)
        .filter(WorkflowEvent.request_id == request_id)
        .order_by(WorkflowEvent.created_at.asc())
        .all()
    )
