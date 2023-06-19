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


