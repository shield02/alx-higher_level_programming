#!/usr/bin/python3
""" Define an empty class"""


class Square:
    """ This is an empty class with size private attribute """
    def __init__(self, size=0):
        """
            Instantiate the class
        Args:
            size: size property of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __eq__(self, other):
        """ Compare equal to"""
        if hasattr(other, 'size'):
            return self.__size == other.__size
        return self.__size == other

    def __ne__(self, other):
        """ Not equal to another square"""
        return self.area() != other.area()

    def __gt__(self, other):
        """ Square greater than another square"""
        if hasattr(other, 'size'):
            return self.__size > other.__size
        return self.area() > other.area()

    def __ge__(self, other):
        """ Square greater than or equal to another square"""
        if hasattr(other, 'size'):
            return self.__size >= other.__size
        return self.area() >= other.area()

    def __lt__(self, other):
        """ Square less than another square"""
        if hasattr(other, 'size'):
            return self.__size < other.__size
        return self.area() < other.area()

    def __le__(self, other):
        """ Square less than or equal to another square"""
        if hasattr(other, 'size'):
            return self.__size <= other.__size
        return self.area() <= other.area()

    @property
    def size(self):
        """
            getter: Get the size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            setter: Set the size property
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            Find the area of the square
        """
        return (self.__size * self.__size)
