from app.workflows.models import WorkflowResult, WorkflowStatus

def assign(
    team: str
) -> WorkflowResult:
    """Assign a workflow to a team."""
    return WorkflowResult(
        status=WorkflowStatus.assigned,
        assigned_team=team,
        action="assign_to_{team}",
    )


def escalate(
    team: str
) -> WorkflowResult:
    """Escalate a workflow to a team."""
    return WorkflowResult(
        status=WorkflowStatus.escalated,
        assigned_team=team,
        action="escalate_to_{team}",
    )