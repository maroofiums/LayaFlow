from app.decisions.models import DecisionResult

ESCALATION_THRESHOLD = 0.80

def should_escalate(decision: DecisionResult) -> bool:
    return decision.escalation_probability >= ESCALATION_THRESHOLD

def requires_immediate_attention(decision: DecisionResult) -> bool:
    return decision.priority.value == "critical"