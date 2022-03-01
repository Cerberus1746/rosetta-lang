from . import lex


def parse_file(script_path):
    lex.lex_file(script_path)
