#!/usr/bin/python3
"""Unittest cases for the base class"""


import os
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(TestCase):
    """Test cases for Base class"""

    def setUp(self):
        Base.__nb_objects = 0

    def test_id(self):
        """Test for id"""
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(-1)
        self.assertEqual(b4.id, -1)
        b5 = Base(123)
        self.assertEqual(b5.id, 123)

    def test_instance(self):
        """Test for instance"""
        b6 = Base()
        self.assertTrue(isinstance(b6, Base))

    def test_type(self):
        """Test for type"""
        b7 = Base()
        self.assertEqual(type(b7), Base)

    def test_to_json_string_empty_list(self):
        """Test static mehod to_json_string with empty list"""
        jl = Base.to_json_string([])
        self.assertEqual(jl, "[]")
    
    def test_to_json_string_none(self):
        """Test static mehod to_json_string with empty list"""
        jn = Base.to_json_string(None)
        self.assertEqual(jn, "[]")

    def test_to_json_string_dict(self):
        """Test static method to_json_string with regular dict"""
        dic = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        jd = Base.to_json_string([dic])
        self.assertTrue(isinstance(dic, dict))
        self.assertTrue(isinstance(jd, str))
        self.assertCountEqual(
            jd, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        )

    def test_to_json_string_wrong_type(self):
        """Test static method to_json_string with wrong types"""
        with self.assertRaises(TypeError) as e:
            Base.to_json_string(3)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries",
            str(e.exception)
        )
        with self.assertRaises(TypeError) as e:
            Base.to_json_string("Hello")
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries",
            str(e.exception)
        )
        with self.assertRaises(TypeError) as e:
            Base.to_json_string(["Hi", "Here"])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries",
            str(e.exception)
        )
        with self.assertRaises(TypeError) as e:
            Base.to_json_string(7.8)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries",
            str(e.exception)
        )
        with self.assertRaises(TypeError) as e:
            Base.to_json_string([2, 1, 3, 4])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries",
            str(e.exception)
        )
        with self.assertRaises(TypeError) as e:
            Base.to_json_string({1: 'hi', 2: 'there'})
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries",
            str(e.exception)
        )
        with self.assertRaises(TypeError) as e:
            Base.to_json_string((9, 0))
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries",
            str(e.exception)
        )
        with self.assertRaises(TypeError) as e:
            Base.to_json_string(True)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries",
            str(e.exception)
        )

    def test_to_json_string_num_of_args(self):
        """Test static method to_json_string 
        with wrong number of arguments"""
        pos_args1 = ("to_json_string() missing 1 required positional argument: " +
              "'list_dictionaries'")
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        self.assertEqual(pos_args1, str(e.exception))

        pos_args2 = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            Base.to_json_string([{3, 5}], [{2, 8}])
        self.assertEqual(pos_args2, str(e.exception))

    def test_save_to_file_type(self):
        """Test class method save_to_file with normal types"""
        rect0 = Rectangle(15, 6, 3, 5)
        rect1 = Rectangle(8, 1)

        Rectangle.save_to_file([rect0, rect1])
        result = ('[{"y": 5, "x": 3, "id": 1, "width": 15, "height": 6},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 8, "height": 1}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(result))

        Rectangle.save_to_file(None)
        result = "[]"
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), result)
        os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), result)

        square0 = Square(13, 1, 5, 4)
        square1 = Square(8, 11)

        Square.save_to_file([square0, square1])
        result = ('[{"id": 4, "size": 13, "x": 1, "y": 5},' +
               ' {"id": 3, "size": 8, "x": 11, "y": 0}]')
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(result))

        Square.save_to_file(None)
        result = "[]"
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), result)
        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), result)

    def test_save_to_file_errors(self):
        """Test class method save_to_file with errors"""
        with self.assertRaises(AttributeError) as e:
            Base.save_to_file([Base(9), Base(5)])
        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'",
            str(e.exception)
        )

        with self.assertRaises(AttributeError) as e:
            Rectangle.save_to_file([3, 4])
        self.assertEqual(
            "'int' object has no attribute 'to_dictionary'",
            str(e.exception)
        )

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file(5)
        self.assertEqual(
            "'int' object is not iterable",
            str(e.exception)
        )

    def test_save_to_file_wrong_args(self):
        """Test class method save_to_file with wrong args"""
        msg1 = ("save_to_file() missing 1 required" +
              " positional argument: 'list_objs'")
        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file()
        self.assertEqual(msg1, str(e.exception))

        msg2 = ("save_to_file() takes 2 positional" +
              " arguments but 3 were given")
        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file([Rectangle(9, 4), Rectangle(8, 9)], 98)
        self.assertEqual(msg2, str(e.exception))

    def test_from_json_to_string_normal_types(self):
        """Test static method from_json_string with normal types"""
        list_dicts = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_dicts)
        json_list_output = Rectangle.from_json_string(json_list_input)

        result = [
            {'width': 10, 'height': 4, 'id': 89},
            {'width': 1, 'height': 7, 'id': 7}
        ]
        self.assertCountEqual(json_list_output, result)
        self.assertEqual(type(json_list_output), list)

        json_list_output_1 = Rectangle.from_json_string('')
        self.assertEqual(json_list_output_1, [])

        json_list_output_2 = Rectangle.from_json_string(None)
        self.assertEqual(json_list_output_2, [])

    def test_from_json_to_string_wrong_types(self):
        """Test static method from_json_string with wrong types"""
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string([8, 9])
        self.assertEqual("json_string must be a string", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string(8)
        self.assertEqual("json_string must be a string", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string(9.6)
        self.assertEqual("json_string must be a string", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string((4, 5))
        self.assertEqual("json_string must be a string", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string({1: 'Hello', 2: 'Hi'})
        self.assertEqual("json_string must be a string", str(e.exception))

if __name__ == "__main__":
    TestCase.main()
