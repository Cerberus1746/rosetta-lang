import pathlib
import dataclasses

from typing import Any

from enum import Enum

import lark
from lark import exceptions


curr_path = pathlib.Path(__file__).parent
parser_file = curr_path / "rosetta.lark"


class RosettaSyntaxError(SyntaxError):
    pass


class Access(Enum):
    PUBLIC = 1
    PRIVATE = 2
    PROTECTED = 4


@dataclasses.dataclass
class Variable:
    access: Access
    name: str
    value: Any


class MainTransformer(lark.Transformer):
    def map(in_dict):
        keys = in_dict[::2]
        values = in_dict[1::2]
        zipped = zip(keys, values)
        return dict(zipped)

    def public(x):
        return Access.PUBLIC

    def private(x):
        return Access.PRIVATE

    def protected(x):
        return Access.PROTECTED

    def ESCAPED_STRING(in_str):
        return in_str[1:-1]

    def TRUE(_):
        return True

    def FALSE(_):
        return False

    def NONE(_):
        return None

    SIGNED_INT = int
    SIGNED_FLOAT = float

    array = list



lark_parser = lark.Lark.open(
    str(parser_file),
    parser="lalr",
    maybe_placeholders=True,
)


def parse(file_path: pathlib.Path, to_parse, *args, **kwargs):
    try:
        return lark_parser.parse(to_parse, *args, **kwargs)
    except(
        exceptions.UnexpectedToken,
        exceptions.UnexpectedCharacters
    ) as parse_error:
        error_tuple = (
            str(file_path.resolve()),
            str(parse_error.line),
            str(parse_error.column),
        )
        error_str = "At: "
        error_str += ":".join(error_tuple)

        if isinstance(parse_error, exceptions.UnexpectedCharacters):
            error_str += "\nexpected:\n  "
            error_str += "\n  ".join(parse_error.allowed)

        error_str += "\n" + str(parse_error)

        raise RosettaSyntaxError(error_str)
