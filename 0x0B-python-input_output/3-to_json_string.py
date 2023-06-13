#!/usr/bin/python3
"""To JSON String module"""
import json


def to_json_string(my_obj):
    """ Represent an object (string) as JSON
        Args:
            my_obj: string object to b serialized
        Raises:
            Nothing
        Return:
            Serialized object
    """
    return json.dumps(my_obj)
