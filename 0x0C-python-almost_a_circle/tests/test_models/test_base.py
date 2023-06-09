#!/usr/bin/python3
"""Unittest cases for the base class"""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        # Base.__nb_objects = 0
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_id(self):
        """Test for id"""
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

    def test_save_to_file_normal_types(self):
        """Test class method save_to_file with normal types"""
        rect0 = Rectangle(15, 6, 3, 5)
        rect1 = Rectangle(8, 1)

        Rectangle.save_to_file([rect0, rect1])
        result = ('[{"y": 5, "x": 3, "id": 1, "width": 15, "height": 6}, ' +
               '  {"y": 0, "x": 0, "id": 2, "width": 8, "height": 1}]')
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
        result = ('[{"id": 4, "size": 13, "x": 1, "y": 5}, ' +
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

        json_list_output_1 = Rectangle.from_json_string('[]')
        self.assertEqual(json_list_output_1, [])

        json_list_output_2 = Rectangle.from_json_string(None)
        self.assertEqual(json_list_output_2, [])

    def test_from_json_to_string_wrong_types(self):
        """Test static method from_json_string with wrong types"""
        msg = ("the JSON object must be str, bytes or " +
                "bytearray, not ")

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string([8, 9])
        self.assertEqual(msg + "list", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string(8)
        self.assertEqual(msg + "int", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string(9.6)
        self.assertEqual(msg + "float", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string((4, 5))
        self.assertEqual(msg + "tuple", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string({1: 'Hello', 2: 'Hi'})
        self.assertEqual(msg + "dict", str(e.exception))

    def test_from_json_to_string_wrong_agrs(self):
        """Test static method from_json_string with wrong args"""
        msg1 = ("from_json_string() missing 1" +
              " required positional argument: 'json_string'")

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string()
        self.assertEqual(msg1, str(e.exception))

        msg2 = ("from_json_string() takes 1 positional" +
            " argument but 2 were given")

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string("Hi", 98)
        self.assertEqual(msg2, str(e.exception))

    def test_create_normal_types(self):
        """Test class method create with normal types"""
        rect1 = Rectangle(3, 5, 1)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual(str(rect1), str(rect2))
        self.assertFalse(rect1 is rect2)
        self.assertFalse(rect1 == rect2)

        square1 = Square(3, 5)
        square1_dictionary = square1.to_dictionary()
        square2 = Square.create(**square1_dictionary)
        self.assertEqual(str(square1), str(square2))
        self.assertFalse(square1 is square2)
        self.assertFalse(square1 == square2)

    def test_create_wrong_types(self):
        """Test class method create with wrong types"""
        with self.assertRaises(TypeError) as e:
            rect1 = "Hello"
            rect2 = Rectangle.create(rect1)
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given",
            str(e.exception)
        )

    def test_load_from_file_normal_types(self):
        """Test class method load_from_file with normal types"""
        rect1 = Rectangle(2, 5, 10, 3)
        rect2 = Rectangle(5, 9)
        rectangles_input = [rect1, rect2]
        Rectangle.save_to_file(rectangles_input)
        rectangles_output = Rectangle.load_from_file()
        for tup in zip(rectangles_input, rectangles_output):
            self.assertEqual(str(tup[0]), str(tup[1]))

        square1 = Square(13, 6)
        square2 = Square(17)
        squares_input = [square1, square2]
        Square.save_to_file(squares_input)
        squares_output = Square.load_from_file()
        for tup in zip(squares_input, squares_output):
            self.assertEqual(str(tup[0]), str(tup[1]))

    def test_load_from_file_missing_file(self):
        """Test class method load_from_file with missing files"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        rectangles_output = Rectangle.load_from_file()
        self.assertEqual(rectangles_output, [])
        squares_output = Square.load_from_file()
        self.assertEqual(squares_output, [])

    def test_load_from_file_wrong_args(self):
        """Test class method load_from_file with wrong args"""
        msg = "load_from_file() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as e:
            list_rectangles_output = Rectangle.load_from_file("Hello")
        self.assertEqual(msg, str(e.exception))

    def test_save_to_file_csv_normal_types(self):
        """Test class method save_to_file_csv with normal types"""
        rect0 = Rectangle(10, 7, 2, 8)
        rect1 = Rectangle(2, 4)

        Rectangle.save_to_file_csv([rect0, rect1])

        result = "id,width,height,x,y\n1,10,7,2,8\n2,2,4,0,0\n"
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(len(f.read()), len(result))

        square0 = Square(9, 3, 1, 12)
        square1 = Square(6, 7)

        Square.save_to_file_csv([square0, square1])

        result = "id,size,x,y\n12,9,3,1\n3,6,7,0\n"
        with open("Square.csv", "r") as f:
            self.assertEqual(len(f.read()), len(result))

    def test_save_to_file_csv_errors(self):
        """Test class method save_to_file_csv with errors"""
        with self.assertRaises(AttributeError) as e:
            Base.save_to_file_csv([Base(3), Base(1)])
        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'",
            str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file_csv([6, 7])
        self.assertEqual(
            "list_objs must be a list of instances",
            str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file_csv(5.9)
        self.assertEqual(
            "list_objs must be a list of instances",
            str(e.exception))

    def test_save_to_file_csv_wrong_args(self):
        """Test class method save_to_file_csv with wrong args"""
        msg1 = ("save_to_file_csv() missing 1 required" +
              " positional argument: 'list_objs'")
        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file_csv()
        self.assertEqual(msg1, str(e.exception))

        msg2 = "save_to_file_csv() takes 2 positional arguments but 3 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file_csv([Rectangle(12, 3), Rectangle(5, 8)], 76)
        self.assertEqual(msg2, str(e.exception))

    def test_load_from_file_csv_missing_file(self):
        """Test class method load_from_file_csv with missing files"""
        # os.remove("Rectangle.csv")
        # os.remove("Square.csv")
        # os.remove("Base.csv")

        rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(rectangles_output, [])

        squares_output = Square.load_from_file_csv()
        self.assertEqual(squares_output, [])

    def test_load_from_file_csv_wrong_args(self):
        """Test class method load_from_file_csv with wrong args"""
        msg = "load_from_file_csv() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as e:
            rectangles_output = Rectangle.load_from_file_csv("Hello")
        self.assertEqual(msg, str(e.exception))

if __name__ == "__main__":
    unittest.main()
