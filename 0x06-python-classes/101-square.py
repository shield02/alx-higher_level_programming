#!/usr/bin/python3
""" Define an empty class"""


class Square:
    """ This is an empty class with size private attribute """
    def __init__(self, size=0, position=(0, 0)):
        """
            Instantiate the class
        Args:
            size: size property of the square
            position: position property of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def __str__(self):
        """ Print the readable details of the object"""
        if self.__size == 0:
            return ''
        else:
            strng = ""
            strng += '\n' * self.__position[1]
            for i in range(0, self.__size):
                strng += ' ' * self.__position[0]
                strng += '#' * self.__size
                strng += '\n'
            return strng[:-1]

    @property
    def size(self):
        """
            getter: Get the size property
        """
        return self.__size

    @property
    def position(self):
        """
            getter: Get the position property
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
            setter: set position and handle errors
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
            Find the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
            Print a square using #
        """
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
