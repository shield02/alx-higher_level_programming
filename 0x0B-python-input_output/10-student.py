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
            Nothing
        Raises:
            Nothing
        Return:
            str: dictionary
        """
        if type(attrs) == list and all(type(el) == str for el in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
