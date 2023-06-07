#!/usr/bin/python3
"""
Module name: print_square
Defines a function that prints a square using #.
"""


def print_square(size):
    """ Prints a square using #
    Args:
        size: (int) length of the square
    Raises:
        TypeError if size is not an integer
        ValueError if size is less than 0
        TypeError if size is a float and is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
