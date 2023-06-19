#!/usr/bin/python3
"""Base class module"""


import json
import csv

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

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation
        Args:
            json_string (str): List of list of dictionaries
        Returns:
            (list): list represented by json_string
        """
        if json_string == "[]" or json_string is None:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the already set attributes
        Uses the update method to assign all attributes
        Args:
            cls (string): class name
            **dictionary (dict): to be used as **kwargs
        Returns:
            (string): 
        """
        if dictionary != {} and dictionary:
            if cls.__name__ == 'Square':
                obj = cls(1)
            else:
                obj = cls(3, 5)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        Args:
            cls (string): current class name using this method
        Returns:
            (list): list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                objs_dict = Base.from_json_string(f.read())
                return [cls.create(**obj) for obj in objs_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list of objects to csv file
        Args:
            list_objs (list): list of class instances inheriting from Base class
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            if list_objs == [] or list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialise list of objects from a csv file
        Args:
            cls (string): current class name using this method
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(f, fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in dic.items())
                              for dic in reader]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []
