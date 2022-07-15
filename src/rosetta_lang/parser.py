import pathlib

import lark
from lark import exceptions


curr_path = pathlib.Path(__file__).parent
parser_file = curr_path / "rosetta.lark"


class RosettaSyntaxError(SyntaxError):
    pass


lark_parser = lark.Lark.open(
    str(parser_file),
    parser="lalr",
    maybe_placeholders=True,
)


def parse(file_path: pathlib.Path, to_parse, *args, **kwargs):
    try:
        return lark_parser.parse(to_parse, *args, **kwargs)
    except (
        exceptions.UnexpectedToken,
        exceptions.UnexpectedCharacters,
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
