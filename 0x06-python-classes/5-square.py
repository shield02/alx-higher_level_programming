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

    def my_print(self):
        """
            Print a square using #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
