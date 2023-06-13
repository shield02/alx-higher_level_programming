#!/usr/bin/python3
"""Object to a text file module"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file
    Args:
        my_obj: string object to b serialized
        filename: string rep of the path to the file
    Raises:
        Nothing
    Return:
        Object represented by JSON string
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
