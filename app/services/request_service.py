from sqlalchemy.orm import Session

from app.database.repository import (
    create_request,
    update_request_decision
)
from app.decisions.engine import DecisionEngine
from app.decisions.schemas import SupportRequest
from app.workflows.orchestrator import WorkflowOrchestrator



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

        decision = self.decision_engine.decide(
            request
        )

        workflow = self.workflow_orchestrator.execute(
            decision
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