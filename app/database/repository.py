from sqlalchemy.orm import Session

from app.database.models import RequestRecord


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