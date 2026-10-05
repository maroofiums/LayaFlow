from app.decisions.models import DecisionResult
from app.workflows.models import WorkflowResult, WorkflowStatus
from app.workflows.router import get_team
from app.workflows.actions import assign, escalate


ESCALATION_THRESHOLD = 0.80

class WorkflowOrchestrator:
    def execute(self, decision: DecisionResult) -> WorkflowResult:
        team = get_team(decision.category)
        if decision.escalation_probability >= ESCALATION_THRESHOLD:
            return escalate(team)
        return assign(team)