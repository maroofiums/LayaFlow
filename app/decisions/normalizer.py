from app.decisions.models import DecisionResult

class DecisionNormalizer:
    """
        Convert Laya's raw output into our application's
        stable DecisionResult format.
    """
    def normalize(self, raw_result) -> DecisionResult:
        print("RAW lAYA RESULT: ")
        print(raw_result)
        raise NotImplementedError(
            "Implement this After inspecting the actual laya output."
        )