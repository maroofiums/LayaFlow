from enum import Enum

from pydantic import BaseModel

class WorkflowStatus(str, Enum):
    pending = "pending"
    assigned = "assigned"
    escalated = "escalated"
    completed = "completed"


class WorkflowResult(BaseModel):
    status: WorkflowStatus
    assigned_team: str | None = None
    action: str
    
