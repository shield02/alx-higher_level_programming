#!/usr/bin/python3
"""Square class module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Instantiate the class
        Args:
            size (int): private instance attribute
        Raises:
            Nothing
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """String description of the class"""
        return str(f"[Square] {self.__size}/{self.__size}")

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size
