#!/usr/bin/python3
"""Search and update module"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line (new_string) of text
    to a file (filename), after (search_string)
    Args:
        filename (str): file path
        search_string (str): specific string to search for
        new_sring (str): text to be inserted
    Raises:
        Nothing
    Return:
        Nothing
    """
    with open(filename, "r+", encoding="utf-8") as f:
        string = ""
        for line in f:
            string += line
            if search_string in line:
                string += new_string
        f.seek(0)
        f.write(string)
