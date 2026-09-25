from fastapi import APIRouter

from app.core.container import decision_engine
from app.decisions.schemas import SupportRequest


router = APIRouter(
    prefix="/api",
    tags=["decisions"],
)


@router.post("/decide")
def decide(request: SupportRequest):

    result = decision_engine.decide(request)

    return {
        "input": request,
        "decision": result
    }