#!/usr/bin/python3
"""Geometry class Module"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """Raise an exception, not implemented
        Args:
            Nothing
        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value
        Args:
            value (int): integer
            name (str): string
        Raises:
            TypeError: value is not an int
            ValueError: value is less or equal to zero
        Returns:
            Nothing
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
