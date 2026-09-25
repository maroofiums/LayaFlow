from enum import Enum

from pydantic import BaseModel


class Category(str, Enum):
    technical = "technical"
    billing = "billing"
    account = "account"
    security = "security"
    general = "general"


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class DecisionResult(BaseModel):
    category: Category
    category_confidence: float

    priority: Priority
    priority_score: float

    escalation_probability: float