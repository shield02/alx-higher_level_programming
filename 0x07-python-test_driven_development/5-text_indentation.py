#!/usr/bin/python3
"""
Module name: text_indentation
Prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """ Prints text with added two newlines
        after each of these characters '.', '?', ':'
    Args:
        text - (string) characters
    Raises:
        TypeError if text is not a string
    Returns:
        Nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".:?":
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])
    print(f"{text}", end="")
