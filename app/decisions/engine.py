from app.core.laya_model import load_laya
from app.decisions.questions import QUESTIONS
from app.decisions.schemas import SupportRequest


class DecisionRequest:

    def __init__(self):
        self.agent = load_laya()

    def decide(self, request: SupportRequest):
        state = {
            "title": request.title,
            "description": request.description
        }

        result = self.agent.predict(
            state,
            QUESTIONS
        )

        return result