from dataclasses import dataclass
from typing import Optional

from . import blocks
from .. import misc_enums


@dataclass
class Class:
    access: misc_enums.Access
    name: str
    inheritance: Optional[str]
    body: blocks.Block


class TypeTransformer:
    def TYPE(x):
        return str(x)

    def type_definition(x):
        return Class(*x)


__all__ = (
    "Class",
    "TypeTransformer",
)
