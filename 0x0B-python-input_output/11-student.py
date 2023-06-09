#!/usr/bin/python3
"""Student class module"""


class Student:
    """Student class definition"""
    def __init__(self, first_name, last_name, age):
        """ Instantiate class
        Args:
            first_name: string rep of first name
            last_name: string rep of last name
            age: integer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary description of the class instance
        Args:
            attrs (str): - Optional, attrs of a class
        Raises:
            Nothing
        Return:
            str: dictionary
        """
        if type(attrs) == list and all(type(el) == str for el in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the class
        Args:
            json (dict): key/value pair of attr name/attribute
        Raises:
            Nothing
        Returns:
            Nothing
        """
        for name, attr in json.items():
            setattr(self, name, attr)
