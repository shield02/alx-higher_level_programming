#!/usr/bin/python3
"""
Module name: say_my_name
Defines a function that prints first name and last name
"""


def say_my_name(first_name, last_name=""):
    """ Print first name and last name.
    Args:
        first_name: String 
        last_name: Strin
    Raises:
        TypeError if the name is not a string
    Returns:
        Nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
