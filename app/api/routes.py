from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.container import (
    request_service,
)
from app.database.database import get_db
from app.database.repository import (
    create_request,
    get_request,
    get_requests,
    update_request_decision,
)
from app.decisions.schemas import SupportRequest
from app.api.schemas import (
    ProcessRequestResponse,
    RequestResponse
)

router = APIRouter(
    prefix="/api",
    tags=["requests"],
)


@router.post("/requests/process", response_model=ProcessRequestResponse)
def process_request(
    request: SupportRequest,
    db: Session = Depends(get_db),
):
    return request_service.process(
        db=db,
        request=request
    )

@router.get("/requests")
def list_requests(
    db: Session = Depends(get_db),
):
    return get_requests(db)


@router.get("/requests/{request_id}", response_model=RequestResponse)
def retrieve_request(
    request_id: int,
    db: Session = Depends(get_db),
):

    request = get_request(db, request_id)

    if request is None:
        raise HTTPException(status_code=404, detail="Request not found")

    return request