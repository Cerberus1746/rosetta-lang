import pathlib

from lark import Lark
from lark import indenter


class TreeIndenter(indenter.Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = ["_LP"]
    CLOSE_PAREN_types = ["_RP"]
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8


curr_path = pathlib.Path(__file__).parent

lark_parser = Lark.open(
    str(curr_path / "rosetta.lark"),
    parser="lalr",
    maybe_placeholders=True,
    regex=True,
    postlex=TreeIndenter(),
)

for curr_file in curr_path.glob("samples/*.roset"):
    with (curr_path / "debug" / f"{curr_file.name}.log").open("w") as debug:
        with curr_file.open() as curr_file_handler:
            try:
                pretty = lark_parser.parse(curr_file_handler.read()).pretty()
                debug.write(pretty)
            except Exception as curr_e:
                debug.write(str(curr_e))
