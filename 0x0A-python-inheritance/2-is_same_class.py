#!/usr/bin/python3
"""Check exact same object module"""


def is_same_class(obj, a_class):
    """Checks for objects that are the same
    Args:
        obj: instance of a class
        a_class: the other class
    Raises:
        Nothing
    Returns:
        True or False
    """
    if type(obj) == a_class:
        return True
    return False
