#!/usr/bin/python3
"""Unittest cases for the square class"""


import io
import contextlib
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        Base.__nb_objects = 0

    def test_attributes(self):
        """Test attributes"""
        square0 = Square(1)
        self.assertEqual(square0.id, 1)

        square1 = Square(5, 3, 4)
        self.assertEqual(square1.height, 5)
        self.assertEqual(square1.width, 5)
        self.assertEqual(square1.x, 3)
        self.assertEqual(square1.y, 4)
        self.assertEqual(square1.id, 2)
    
    def test_str_rep(self):
        """Test __str__ representation"""
        square = Square(9, 4, 5, 6)
        self.assertEqual(str(square), "[Square] (6) 4/5 - 9")

    def test_inheritance(self):
        """Test inheritance"""
        square = Square(6)
        self.assertTrue(isinstance(square, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(square, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_missing_args(self):
        """Test for missing args"""
        with self.assertRaises(TypeError) as e:
            Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(e.exception)
        )

    def test_inherited_from_rect(self):
        """Test Square for methods inherited from Rectangle"""
        square1 = Square(9)
        self.assertEqual(square1.area(), 81)

        square2 = Square(4, 1, 2, 5)
        square2.update(7)

        self.assertEqual(square2.id, 7)
        flush = io.StringIO()

        square3 = Square(4)
        with contextlib.redirect_stdout(flush):
            square3.display()
        msg = flush.getvalue()
        result = "####\n####\n####\n####\n"
        self.assertEqual(msg, result)

    def test_size(self):
        """Test for size attribute"""
        square1 = Square(8)
        self.assertEqual(square1.size, 8)

        square2 = Square(9, 8, 7, 2)
        self.assertEqual(square2.size, 9)

if __name__ == '__main__':
    unittest.main()
