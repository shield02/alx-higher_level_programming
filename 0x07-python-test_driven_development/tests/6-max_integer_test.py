"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer function"""

    def test_empty_list(self):
        """Test for empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Test a list with one element"""
        one_list_element = [10]
        self.assertEqual(max_integer(one_list_element), 10)

    def test_list_of_floats(self):
        """Test a list of floats"""
        floats_list = [12.4, 8.3, 5.5, 6.1]
        self.assertEqual(max_integer(floats_list), 12.4)

    def test_list_of_negative_integers(self):
        """Test for max negative int"""
        neg_int = [-2, -4, -19, -1, -6]
        self.assertEqual(max_integer(neg_int), -1)

    def test_list_of_int_and_floats(self):
        """Test a list with int and floats"""
        int_floats = [1.4, 6, 3.1, 9, 10.2, 4.1]
        self.assertEqual(max_integer(int_floats), 10.2)

    def test_string(self):
        """Test a string."""
        string = "Python"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Testing", "in", "python", "language"]
        self.assertEqual(max_integer(strings), "python")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_ordered_list(self):
        """Test a list of ordered integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test a list of unordered integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list that begin with the max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

if __name__ == '__main__':
    unittest.main()
