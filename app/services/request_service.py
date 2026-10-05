from sqlalchemy.orm import Session

from app.database.repository import (
    create_request,
    update_request_decision
)
from app.decisions.engine import DecisionEngine
from app.decisions.schemas import SupportRequest
from app.workflows.orchestrator import WorkflowOrchestrator
from app.workflows.events import record_event


class RequestService:
    def __init__(
        self,
        decision_engine: DecisionEngine,
        workflow_orchestrator: WorkflowOrchestrator,
    ):
        self.decision_engine = decision_engine
        self.workflow_orchestrator = workflow_orchestrator

    def process(
        self,
        db: Session,
        request: SupportRequest
    ):

        db_request = create_request(
            db = db,
            title = request.title,
            description = request.description,
        )

        record_event(
            db=db,
            request_id=db_request.id,
            event_type="request_created",
            description="Support request created."
        )

        record_event(
            db=db,
            request_id=db_request.id,
            event_type="processing_started",
            description="Support send to decision engine."
        )

        decision = self.decision_engine.decide(
            request
        )

        record_event(
            db=db,
            request_id=db_request.id,
            event_type="decision_made",
            description=(
                f"Category={decision.category.value}, "
                f"Priority={decision.priority.value}, "
                f"EscalationProbability={decision.escalation_probability.value:.3f}, "
            )
        )

        workflow = self.workflow_orchestrator.execute(
            decision
        )


        record_event(
            db=db,
            request_id=db_request.id,
            event_type=workflow.status.value,
            description=workflow.action
        )


        update_request_decision(
            db = db,
            request = db_request,
            category = decision.category,
            priority = decision.priority,
            escalation_probability = decision.escalation_probability,
            workflow_status = decision.workflow_status,
            assigned_team = decision.assigned_team,
            workflow_action = decision.workflow_action,
        )


        return {
            "id": request.id,
            "request": request,
            "decision": decision,
            "workflow": workflow,
            
        }