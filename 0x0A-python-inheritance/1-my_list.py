#!/usr/bin/python3
"""Inherit from a list"""


class MyList(list):
    """A simple class that inherits another class"""
    def print_sorted(self):
        """Prints a sorted list
        Args:
            Nothing
        Raises:
            Nothing
        Returns:
            Sorted list
        """
        sort_list = self[:]
        print(f"{sort_list.sort()}")
