#!/usr/bin/python3
"""Append to a file module"""


def append_write(filename="", text=""):
    """ Append a string to the end of a file
        Args:
            filename: string path to the file
            text: string to be appended
        Raise:
            Nothing
        Return:
            int: number of characters
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
