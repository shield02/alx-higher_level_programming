#!/usr/bin/python3
"""Rectangle base module"""

from models.base import Base

class Rectangle(Base):
    """Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Accessor for the width variable"""
        return self.__width

    @property
    def height(self):
        """Accessor for the height variable"""
        return self.__height

    @property
    def x(self):
        """Accessor for the x variable"""
        return self.__x

    @property
    def y(self):
        """Accessor for the y variable"""
        return self.__y

    @width.setter
    def width(self, width):
        """Set the value of the width attribute"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @height.setter
    def height(self, height):
        """Set the value of the height attribute"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @x.setter
    def x(self, x):
        """Set the value of x attribute"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @y.setter
    def y(self, y):
        """Set the value of y attibute"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Calculate the area of the rectangle"""
        return int(self.__width * self.__height)

    def display(self):
        """Print the rectangle instance using # character"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Print string representation of the rectangle class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """Assigns arguments to each attribute
        Args:
            *args: any number of arguments
                    1st arg - id
                    2nd arg - width
                    3rd arg - height
                    4th arg - x
                    5th arg - y
        """
        if len(args) != 0 and args is not None:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an int")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
            
