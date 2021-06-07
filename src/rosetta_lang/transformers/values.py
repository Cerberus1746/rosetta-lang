class ValuesTransformer:
    def map(in_dict):
        keys = in_dict[::2]
        values = in_dict[1::2]
        zipped = zip(keys, values)
        return dict(zipped)

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
