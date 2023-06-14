#!/usr/bin/python3


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
