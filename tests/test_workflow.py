import pytest

from app.workflows.models import WorkflowStatus
from app.workflows.state_machine import transition


def test_pending_to_processing():

    result = transition(
        WorkflowStatus.pending,
        WorkflowStatus.processing,
    )

    assert result == WorkflowStatus.processing


def test_processing_to_assigned():

    result = transition(
        WorkflowStatus.processing,
        WorkflowStatus.assigned,
    )

    assert result == WorkflowStatus.assigned


def test_processing_to_escalated():

    result = transition(
        WorkflowStatus.processing,
        WorkflowStatus.escalated,
    )

    assert result == WorkflowStatus.escalated


def test_completed_cannot_transition():

    with pytest.raises(ValueError):

        transition(
            WorkflowStatus.completed,
            WorkflowStatus.processing,
        )