from rosetta_lang import base_types


def test_iterators_in_base(debug_log_code):
    debug_log_code(list(map(lambda x: x.values(), base_types.RosettaBase().all_tokens.values())))
