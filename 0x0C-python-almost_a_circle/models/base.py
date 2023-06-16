#!/usr/bin/python3
"""Base class module"""


class Base:
    """Base class for the project
    To manage id attribute project wide and to avoid code duplication
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        Args:
            id (int): id attribue
        Raises:
            Nothing
        Return:
            Nothing
        """
        if id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = id
