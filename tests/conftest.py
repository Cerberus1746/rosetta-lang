import logging
import os
from pathlib import Path

import pytest

import lark

from rosetta_lang import parser
from rosetta_lang.transformers import main


current_folder = Path(__file__).parent

parser_with_all_symbols = lark.Lark.open(
    str(parser.parser_file),
    parser="lalr",
    maybe_placeholders=True,
    keep_all_tokens=True,
)

parser_with_transformer = lark.Lark.open(
    str(parser.parser_file),
    parser="lalr",
    maybe_placeholders=True,
    transformer=main.MainTransformer,
)

work_dir = Path(os.getenv("TOX_WORK_DIR", current_folder))
current_tox_env = os.getenv("TOX_ENV_NAME", "")

log_file = work_dir / current_tox_env / "testing.log.md"

file_logger = logging.FileHandler(log_file, "w")


@pytest.fixture(scope="session")
def curr_logger():
    curr_logger = logging.getLogger()
    curr_logger.setLevel(logging.DEBUG)
    curr_logger.addHandler(file_logger)

    curr_logger.debug("# PyTest\n")

    return curr_logger


@pytest.fixture(scope="session")
def open_text_to_parse():
    def file_to_open(file_name: str):
        path_to_open = current_folder / "resources/language_files" / file_name
        with path_to_open.open() as orig_text:
            return orig_text.read(), path_to_open

    return file_to_open


@pytest.fixture(scope="session")
def debug_log_code(curr_logger):
    def inner_debug_log_code(curr_title, text_to_parse, parse_result):
        curr_logger.debug(f"## {curr_title}")
        curr_logger.debug("Code to be parsed:\n```\n" + text_to_parse + "```")

        if hasattr(parse_result, "pretty"):
            curr_logger.debug("Result:\n```\n" + parse_result.pretty() + "```")
        else:
            curr_logger.debug("Result:\n```\n" + repr(parse_result) + "```")

    return inner_debug_log_code


@pytest.fixture(scope="session")
def parse_test(open_text_to_parse, debug_log_code):
    def inner_parse_test(test_name, file_name):
        to_parse, opened_file = open_text_to_parse(file_name)
        result = parser_with_all_symbols.parse(to_parse)
        debug_log_code(test_name, to_parse, result)

    return inner_parse_test


@pytest.fixture(scope="session")
def parse_transform(open_text_to_parse, debug_log_code):
    def inner_parse_test(test_name, file_name):
        to_parse, opened_file = open_text_to_parse(file_name)
        result = parser_with_transformer.parse(to_parse)
        debug_log_code(test_name, to_parse, result)

    return inner_parse_test
