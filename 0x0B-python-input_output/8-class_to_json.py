#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj):
    """Dictionary description of simple data strutures
    Args:
        obj: instance of a class
    Raises:
        Nothing
    Return:
        str: dictionary
    """
    return obj.__dict__
