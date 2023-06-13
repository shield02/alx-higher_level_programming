#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """ Convert a JSON string to an object
    Args:
        my_obj: string object to b serialized
    Raises:
        Nothing
    Return:
        Object represented by JSON string
    """
    return json.loads(my_str)
