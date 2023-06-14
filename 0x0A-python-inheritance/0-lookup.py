#!/usr/bin/python3
"""Instance attributes and methods module"""


def lookup(obj):
    """List all avialable attributes and methods
    Args:
        obj: class instance
    Raises:
        Nothing
    Returns:
        A list
    """
    return dir(obj)
