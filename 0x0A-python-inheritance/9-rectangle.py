#!/usr/bin/python3
"""Rectangle class module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Instantiate the class
        Args:
            width (int): private instance attribute
            height (int): privat instance attribute
        Raises:
            Nothing
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """String description of the class"""
        return str(f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height
