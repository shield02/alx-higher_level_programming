#!/usr/bin/python3
"""Add attribute module"""


def add_attribute(obj, attr, val):
    """"Add a new attribute to an object if possible
    or raise and exception
    Args:
        obj: object
        attr: attribute
        val: value
    Raises:
        TypeError: if attribute cannot be added
    Return:
        Nothing
    """
    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
