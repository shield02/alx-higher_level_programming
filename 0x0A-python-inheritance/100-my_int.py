#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """MyInt class inheriting int
    Reverses the behaviour of == and !=
    """
    def __eq__(self, other):
        """Reverse equality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Reverse inequality"""

        return super().__eq__(other)
