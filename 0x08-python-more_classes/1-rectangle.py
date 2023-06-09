#!/usr/bin/python3
""" Define an empty Rectangle class"""


class Rectangle:
    """ Rectangle class"""

    def __init__(self, width=0, height=0):
        """ Initialize class with width and height"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """ Get the height property"""
        return self.__height

    @property
    def width(self):
        """ Get the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width property"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ Set the height property"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
