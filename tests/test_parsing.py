def test_function(parse_test):
    parse_test("Function", "function_test.roset")


def test_variable(parse_test):
    parse_test(
        "Variable",
        "variable_test.roset",
    )


def test_complete_language(parse_test):
    parse_test(
        "Complete Language",
        "complete_language_test.roset",
    )


def test_indexing(parse_test):
    parse_test(
        "Indexing Test",
        "indexing_test.roset",
    )


def test_variable_in_class(parse_test):
    parse_test(
        "Variable in Class",
        "variable_in_class.roset",
    )
