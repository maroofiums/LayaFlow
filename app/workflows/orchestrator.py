from app.decisions.models import DecisionResult
from app.workflows.models import WorkflowResult, WorkflowStatus
from app.workflows.router import get_team



class WorkflowOrchestrator:
    def execute(self, decision: DecisionResult) -> WorkflowResult:
        team = get_team(decision.category)
        if decision.escalation_probability >= 0.80:
            return WorkflowResult(
                status=WorkflowStatus.escalated,
                assigned_team=team,
                action=f"escalate_to_{team}"         
            )
        return WorkflowResult(
            status=WorkflowStatus.assigned,
            assigned_team=team,
            action=f"assign_to_{team}"
        )