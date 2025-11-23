from typing import Dict
import re
from .operator import Operator, OperatorType


class Initial(Operator):
    """Operator that converts words into initials while preserving prefix characters."""

    def operate(self, text: str, params: Dict = None) -> str:
        # Normalize whitespace
        text = text.strip()
        if not text:
            return ""

        words = re.split(r"\s+", text)
        results = []

        for word in words:
            prefix = ""
            initial_char = None

            # Separate prefix and first alphanumeric char
            for ch in word:
                if ch.isalnum():
                    initial_char = ch.upper()
                    break
                else:
                    prefix += ch

            if initial_char:
                results.append(f"{prefix}{initial_char}.")
            else:
                # No alphanumeric char found — output unchanged
                results.append(prefix)

        return " ".join(results)

    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
