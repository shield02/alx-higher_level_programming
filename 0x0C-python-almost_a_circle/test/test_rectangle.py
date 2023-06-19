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
            rect = Rectangle(9, 5)
            rect.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given",
            str(e.exception)
        )

    def test_display(self):
        """Test public method display"""
        flush = io.StringIO()
        rect = Rectangle(4, 5)
        with contextlib.redirect_stdout(flush):
            rect.display()
        s = flush.getvalue()
        result = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, result)

    def test_display_wrong_args(self):
        """Test public method display with wrong args"""
        with self.assertRaises(TypeError) as e:
            rect = Rectangle(11, 5)
            rect.display(11)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given",
            str(e.exception)
        )

    def test_string_rep(self):
        """Test __str__ representation"""
        flush = io.StringIO()
        rect = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(flush):
            print(rect)
        s = flush.getvalue()
        result = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, result)

    def test_display_x_y(self):
        """Test public method display with x and y"""
        flush = io.StringIO()
        rect = Rectangle(5, 2, 4, 4)
        with contextlib.redirect_stdout(flush):
            rect.display()
        s = flush.getvalue()
        result = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, result)

    def test_update(self):
        """Test public method update"""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual(rect.id, 89)
        rect.update(89, 2)
        self.assertEqual(rect.width, 2)
        rect.update(89, 2, 3)
        self.assertEqual(rect.height, 3)
        rect.update(89, 2, 3, 4)
        self.assertEqual(rect.x, 4)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(rect.y, 5)
        rect.update()
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_wrong_types(self):
        """Test public method update with wrong types"""
        rect = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as e:
            rect.update("hi")
        self.assertEqual("id must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            rect.update(65, 89, "hi")
        self.assertEqual("height must be an integer", str(e.exception))

    def test_update_kwargs(self):
        """Test public method update with kwargs"""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(height=1)
        self.assertEqual(rect.height, 1)
        rect.update(x=1, height=2, y=3, width=4)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.height, 2)

    def test_update_kwargs_wrong_types(self):
        """Test public method update with wrong types in kwargs"""
        rect = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as e:
            rect.update(id='hi')
        self.assertEqual("id must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            rect.update(height=65, x=2, width="hi")
        self.assertEqual("width must be an integer", str(e.exception))

    def test_to_dictionary(self):
        """Test public method to_dictionary"""
        rect1 = Rectangle(10, 2, 1, 9)
        rect1_dictionary = rect1.to_dictionary()
        test_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(rect1_dictionary), len(test_dictionary))
        self.assertEqual(type(rect1_dictionary), dict)

        rect2 = Rectangle(1, 1)
        rect2.update(**rect1_dictionary)
        rect2_dictionary = rect2.to_dictionary()
        self.assertEqual(len(rect1_dictionary), len(rect2_dictionary))
        self.assertEqual(type(rect2_dictionary), dict)
        self.assertFalse(rect1 == rect2)

    def test_to_dictionary_wrong_args(self):
        """Test for public method to_dictionary with wrong args"""
        msg = "to_dictionary() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as e:
            rect = Rectangle(10, 2, 1, 9)
            rect.to_dictionary("Hi")
        self.assertEqual(msg, str(e.exception))

if __name__ == '__main__':
    unittest.main()
