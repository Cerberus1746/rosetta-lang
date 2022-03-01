import dataclasses

from typing import Any, Type


@dataclasses.dataclass
class Token:
    _value: Any = dataclasses.field(repr=False, init=False)

    name: str
    rule: str
    start: int
    end: int
    py_type: Type

    @property
    def value(self):
        return self._value

    @property.setter
    def value(self, new_value):
        if self.py_type:
            self._value = self.py_type(new_value)
        else:
            self._value = new_value

