import lark

from . import values, types
from .. import misc_enums


class MainTransformer(
    values.ValuesTransformer, types.TypeTransformer, lark.Transformer
):
    def public(x):
        return misc_enums.Access.PUBLIC

    def private(x):
        return misc_enums.Access.PRIVATE

    def protected(x):
        return misc_enums.Access.PROTECTED
