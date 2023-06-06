#!/usr/bin/python3
""" Example of a locked class"""


class LockedClass:
    """ This is a locked class. An instance of this
    class cannot be dynamically created, except the
    new instance attribute is called first_name
    """

    __slots__ = ["first_name"]
