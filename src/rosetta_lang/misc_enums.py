"""
Module with miscelaneous enumerators

:author: Leandro (cerberus1746) Benedet Garcia
:date: 2021-06-06
"""
import enum


class Access(enum.Enum):
    """
    Enumerator representing the access of variables, classes and functions.

    :param value: the number representing the enum
    :param type: :class:`python:int`

    :var PUBLIC: Things that will be accessible anywhere
    :var PRIVATE: Things that will be only available in the current context
    :var PROTECTED: Things that will be only available in the current context
                    and trough inheritance.
    """

    PUBLIC = 0b0
    PRIVATE = 0b1
    PROTECTED = 0b10
