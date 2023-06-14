#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """Check for instance of a class that inherited from another class
    Args:
        obj: instance of a class
        a_class: a class
    Raises:
        Nothing
    Returns:
        True or False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
