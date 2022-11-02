#!/usr/bin/python3
"""define a class"""


class Square:
    """initialize an object"""

    def __init__(self, size=0):

        self.__size = size
        """handling exceptions"""
        try:
            assert type(size) == int
        except TypeError:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")