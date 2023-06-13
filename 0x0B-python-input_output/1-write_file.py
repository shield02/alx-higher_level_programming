#!/usr/bin/python3
"""write file function mmodule"""


def write_file(filename="", text=""):
    """ Write a string to a file
        Args:
            filename: string path of the file
            text: string to be written to file
        Raises:
            Nothing
        Return:
            int: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
