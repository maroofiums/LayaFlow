CATEGORY_QUESTION = {
    "type": "choice",
    "instructions": "What category best describes this support request?",
    "criteria": {
        "technical": "software, infrastructure, API, database, deployment, system problems",
        "billing": "payments, invoices, charges, refunds, subscriptions",
        "account": "login, password, profile, account access",
        "security": "security incidents, suspicious activity, unauthorized access",
        "general": "questions that do not fit the other categories",
    },
}


PRIORITY_QUESTION = {
    "type": "choice",
    "instructions": "How urgent is this request?",
    "criteria": {
        "low": "minor issue with little or no immediate impact",
        "medium": "issue affecting normal work but with a workaround",
        "high": "major operational impact requiring prompt attention",
        "critical": "severe production impact, outage, or major security incident",
    },
}


ESCALATION_QUESTION = {
    "type": "noul",
    "instructions": (
        "Should this support request be escalated to a specialized "
        "human team?"
    ),
}


QUESTIONS = {
    "category": CATEGORY_QUESTION,
    "priority": PRIORITY_QUESTION,
    "escalate": ESCALATION_QUESTION,
}