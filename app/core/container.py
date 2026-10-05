from app.decisions.engine import DecisionEngine
from app.workflows.orchestrator import WorkflowOrchestrator
from app.services.request_service import RequestService


decision_engine = DecisionEngine()
workflow_orchestrator = WorkflowOrchestrator()
request_service = RequestService(
    decision_engine=decision_engine,
    workflow_orchestrator=workflow_orchestrator
)