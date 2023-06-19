#!/usr/bin/python3
"""Square base module"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class
    Inherit the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Sqaure constructor
        Args:
            size (int): 
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print string representation of the square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """Accessor for the size variable"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Set the value of the size attribute
        Args:
            value (int): value for both width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square class using either the args or kwargs
        Args:
            *args (list): list of ordered arguments
                1st arg: id
                2nd arg: size
                3rd arg: x
                4th arg: y
            *kwargs (dict): key/value pairs of attribute/value
        """
        if len(args) > 0 and args is not None:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an int")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for attr, value in kwargs.items():
                if attr == 'id':
                    if type(value) is not int and value is not None:
                        raise TypeError("id must be an int")
                    self.id = value
                if attr == 'size':
                    self.size = value
                if attr == 'x':
                    self.x = value
                if attr == 'y':
                    self.y = value

    def to_dictionary(self):
        """Dictionary representation of the square class
        Returns:
            (dict): key/value pairs of attribute/value
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
