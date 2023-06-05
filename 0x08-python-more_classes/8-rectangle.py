#!/usr/bin/python3
""" Define an empty Rectangle class"""


class Rectangle:
    """ Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialize class with width and height"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ String representation of the class"""
        if self.width and self.height:
            return "\n".join([str(self.print_symbol) * self.width]
                             * self.height)
        return ""

    def __repr__(self):
        """ String representation of the class object
        this can be used with eval() to recreate a new instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ String message that comes when a class is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ Get the width property"""
        return self.__width

    @property
    def height(self):
        """ Get the height property"""
        return self.__height

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

    def area(self):
        """ Calculate the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """ Calculate the perimeter of the rectangle"""
        if self.width and self.height:
            return 2*(self.width + self.height)
        return 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Find the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
