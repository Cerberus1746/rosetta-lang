from dataclasses import dataclass
from typing import Any
import lark

from . import values, types, maths, functions, blocks
from .. import misc_enums


@dataclass
class Statement:
    name: str
    atom: Any


class MainTransformer(
    values.ValuesTransformer,
    types.TypeTransformer,
    lark.Transformer,
    maths.MathTransformer,
    functions.FunctionTransformer,
):
    def PUBLIC(x):
        return misc_enums.Access.PUBLIC

    def PRIVATE(x):
        return misc_enums.Access.PRIVATE

    def PROTECTED(x):
        return misc_enums.Access.PROTECTED

    def block(x):
        return blocks.Block(x)

    def statement(x):
        return Statement(*x)

    start = block

__all__ = (
    "Statement",
    "MainTransformer",
)
