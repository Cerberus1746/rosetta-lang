from dataclasses import dataclass
from typing import Any, List, Optional

from .. import misc_enums
from . import blocks


@dataclass
class FunctionArg:
    type: Any
    name: str
    value: Any
    is_array: bool
    is_map: bool


@dataclass
class Function:
    access: misc_enums.Access
    name: str
    ret_type: Any
    args: List[FunctionArg]
    function_body: Optional[blocks.Block]


class FunctionTransformer:
    def function(x):
        function_args = []
        function_body = None

        access, ret_type, name, *rest = x
        for curr_rest in rest:
            if isinstance(curr_rest, FunctionArg):
                function_args.append(curr_rest)
            elif isinstance(curr_rest, blocks.Block):
                function_body = curr_rest

        return Function(access, name, ret_type, function_args, function_body)

    def map_arg(x):
        return FunctionArg(*x, False, True)

    def array_arg(x):
        return FunctionArg(*x, True, False)

    def regular_arg(x):
        return FunctionArg(*x, False, False)


__all__ = (
    "FunctionArg",
    "Function",
    "FunctionTransformer",
)
