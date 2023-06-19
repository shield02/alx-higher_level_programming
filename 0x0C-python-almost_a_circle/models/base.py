#!/usr/bin/python3
"""Base class module"""


import json

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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string serialization of list of dictionaries
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            JSON (str): 
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list of objects to file
        Args:
            cls (string): class name
            list_objs (list): list of class instances inheritng Base class
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                objs_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(objs_dict))
