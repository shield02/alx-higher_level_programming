#!/usr/bin/python3
"""Read a file and print to stdout"""


def read_file(filename=""):
    """ A function to read content of a file and print to stdout
        Args:
            filename: string path of the file
        Raises:
            Nothing
        Return:
            Nothing
    """

    with open(filename) as f:
        line = f.read()
        print(line, end="")
    # print()
