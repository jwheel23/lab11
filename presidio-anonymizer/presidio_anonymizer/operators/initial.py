from typing import Dict
from .operator import Operator, OperatorType


class Initial(Operator):
    """Operator that converts words to initials (e.g., John Smith → J. S.)."""

    def operate(self, text: str, params: Dict = None) -> str:
        words = text.strip().split()
        initials = [w[0].upper() + "." for w in words if w[0].isalnum()]
        return " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
