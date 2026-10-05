from datetime import datetime

from pydantic import BaseModel


class WorkflowResponse(BaseModel):
    status: str
    assigned_team: str | None
    action: str


class ProcessRequestResponse(BaseModel):
    id: int
    request: dict
    decision: dict
    workflow: WorkflowResponse


class RequestResponse(BaseModel):
    id: int
    title: str
    description: str

    category: str | None
    priority: str | None
    escalation_probability: float | None

    workflow_status: str | None
    assigned_team: str | None
    workflow_action: str | None

    created_at: datetime