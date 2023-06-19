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
            str(e.exception)
        )

        msg = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            Rectangle()
        self.assertEqual(msg, str(e.exception))

    def test_inheritance(self):
        """Test for inheritance"""
        rect1 = Rectangle(7, 5)
        self.assertTrue(isinstance(rect1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_wrong_attributes(self):
        """Test wrong attributes."""
        with self.assertRaises(TypeError) as e:
            Rectangle("Hello", 2)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle(2, "World")
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, "Foo", 3)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 2, "Bar")
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Rectangle(2, -3)
        self.assertEqual("height must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Rectangle(2, 8, 9, -65)
        self.assertEqual("y must be >= 0", str(e.exception))

    def test_area_normal_types(self):
        """Test public method area with normal types"""
        rect1 = Rectangle(3, 2)
        self.assertEqual(rect1.area(), 6)
        rect2 = Rectangle(75, 2)
        self.assertEqual(rect2.area(), 150)
        rect3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect3.area(), 56)

    def test_area_wrong_args(self):
        """Test public method area with wrong args"""
        with self.assertRaises(TypeError) as e:
            rect1 = Rectangle(9, 5)
            rect1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given",
            str(e.exception)
        )

    def test_display(self):
        """Test public method display"""
        flush = io.StringIO()
        rect1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(flush):
            rect1.display()
        s = flush.getvalue()
        result = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, result)

if __name__ == '__main__':
    unittest.main()
