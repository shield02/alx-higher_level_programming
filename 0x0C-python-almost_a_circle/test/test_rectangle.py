#!/usr/bin/python3
"""Unittest cases for the rectangle class"""


import io
import contextlib
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        Base.__nb_objects = 0

    def test_id(self):
        """Test for id."""
        rect0 = Rectangle(1, 2)
        self.assertEqual(rect0.id, 1)
        rect1 = Rectangle(2, 3)
        self.assertEqual(rect1.id, 2)
        rect2 = Rectangle(3, 4)
        self.assertEqual(rect2.id, 3)
        rect3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect3.id, 12)
        rect4 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(rect4.id, 34)
        rect5 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(rect5.id, -5)
        rect6 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(rect6.id, 9)

    def test_attribute_values(self):
        """Test for attributes values"""
        rect1 = Rectangle(8, 3)
        self.assertEqual(rect1.width, 8)
        self.assertEqual(rect1.height, 3)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

        rect2 = Rectangle(14, 5, 3, 1, 24)
        self.assertEqual(rect2.width, 14)
        self.assertEqual(rect2.height, 5)
        self.assertEqual(rect2.x, 3)
        self.assertEqual(rect2.y, 1)

    def test_missing_arguments(self):
        """Test for missing arguments"""
        with self.assertRaises(TypeError) as e:
            Rectangle(7)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

        msg = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            Rectangle()
        self.assertEqual(msg, str(e.exception))

if __name__ == '__main__':
    unittest.main()
