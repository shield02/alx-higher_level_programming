#!/usr/bin/python3
"""Check same class or inherited module"""


def is_kind_of_class(obj, a_class):
    """Checks if object is instance of class
    Args:
        obj: instance of a class
        a_class: a class
    Raises:
        Nothing
    Returns:
        True or False
    """
    return isinstance(obj, a_class)
