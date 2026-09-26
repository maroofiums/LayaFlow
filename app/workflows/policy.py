from pydantic import BaseModel

from app.decisions.models import DecisionResult
from app.decisions.policies import (
    should_escalate,
    requires_immediate_attention
)

class WorkflowDecision(BaseModel):
    escalate: bool
    immediate_attention: bool


def apply_policy(
    decision: DecisionResult
) -> WorkflowDecision:
    
    return WorkflowDecision(
        escalate=should_escalate(decision=decision),
        immediate_attention=requires_immediate_attention(decision=decision)
    )