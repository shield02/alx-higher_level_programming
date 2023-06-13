#!/usr/bin/python3
"""Object from JSON file module"""
import json


def load_from_json_file(filename):
    """Create an object from JSON file
    Args:
        filename: string rep of the path to the file
    Raise:
        Nothing
    Return:
        String object
    """
    with open(filename) as f:
        return json.load(f)
