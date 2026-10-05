from sqlalchemy.orm import Session

from app.database.repository import create_event


def record_event(
    db: Session,
    request_id: int,
    event_type: str,
    description: str | None = None
):

    return create_event(
        db=db,
        request_id=request_id,
        event_type=event_type,
        description=description
    )