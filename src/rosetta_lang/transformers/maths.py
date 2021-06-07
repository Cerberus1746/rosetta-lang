from dataclasses import dataclass
from typing import Any


@dataclass
class Math:
    left: Any
    operator: str
    right: Any


class MathTransformer:
    def mathematical_operation(x):
        return Math(*x)

    def plus(_):
        return "+"

    def minus(_):
        return "-"

    def division(_):
        return "/"

    def squared(_):
        return "**"

    def multiplication(_):
        return "*"


__all__ = (
    "Math",
    "MathTransformer",
)
