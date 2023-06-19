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
