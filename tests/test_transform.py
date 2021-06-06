def test_function(parse_transform):
    parse_transform("Function", "function_test.roset")


def test_variable(parse_transform):
    parse_transform(
        "Variable",
        "variable_test.roset",
    )


def test_complete_language(parse_transform):
    parse_transform(
        "Complete Language",
        "complete_language_test.roset",
    )


def test_indexing(parse_transform):
    parse_transform(
        "Indexing Test",
        "indexing_test.roset",
    )


def test_variable_in_class(parse_transform):
    parse_transform(
        "Variable in Class",
        "variable_in_class.roset",
    )
