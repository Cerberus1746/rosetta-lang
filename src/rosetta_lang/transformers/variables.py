import dataclasses
from typing import Any

from .. import misc_enums

@dataclasses.dataclass
class SetVariable:
    name: str
    in_constructor: bool
    is_optional: bool


@dataclasses.dataclass
class Variable:
    set_var: SetVariable
    access: misc_enums.Access
    value: Any


class VariableTransformer:
    def VAR(x):
        return str(x)

    def var_set(x):
        return list(x)

    def optional_in_constructor(x):
        return SetVariable(x[0], True, True)

    def set_in_constructor(x):
        return SetVariable(x[0], True, False)

    def regular_var(x):
        return SetVariable(x[0], False, False)

    def variable(x):
        instanced_var_list = []
        var_access, var_type, *var_list = x
        for curr_var in var_list:
            instanced_var_list.append(Variable(curr_var, var_access, var_type))

        return instanced_var_list
