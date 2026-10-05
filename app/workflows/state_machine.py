from app.workflows.models import WorkflowStatus

VALID_TRANSATIONS = {
    WorkflowStatus.pending: {
        WorkflowStatus.processing,
    },
    WorkflowStatus.processing: {
        WorkflowStatus.assigned,
        WorkflowStatus.escalated,
    },
    WorkflowStatus.assigned: {
        WorkflowStatus.completed,
    },
    WorkflowStatus.escalated:{
        WorkflowStatus.assigned,
    },
    WorkflowStatus.completed: set(),
}


def can_transition(
    current: WorkflowStatus,
    target: WorkflowStatus,
) -> bool:
    """Check if a transition from current to target is valid."""
    return target in VALID_TRANSATIONS[current]


def transition(
    current: WorkflowStatus,
    target: WorkflowStatus,
) -> WorkflowStatus:
    """Transition from current to target if valid, else raise ValueError."""
    if not can_transition(current, target):
        raise ValueError(f"Invalid transition from {current} to {target}")
    return target