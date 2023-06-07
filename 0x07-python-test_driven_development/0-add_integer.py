#!/usr/bin/python3
"""
    Module for adding two integers not any other type
    Defines the fuctionality of adding two integers that are integers
"""


def add_integer(a, b=98):
    """
        This function adds two numbers
        Raise type error if a and b are not int or float type
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
