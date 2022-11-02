#!/usr/bin/python3
"""define a class"""


class Square:
    """
    you are not allowed to import a module
    """
    def __init__(self, size=0):
        """
        Instantiation with optional size
        size must be an integer,
        otherwise raise a TypeError exception with the message
        size must be an integer
        if size is less than 0,
        raise a ValueError exception with the
        message size must be >= 0
        private instance attribute
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            """Public instance method tha returns square area"""
            return (self.__size * self._size)