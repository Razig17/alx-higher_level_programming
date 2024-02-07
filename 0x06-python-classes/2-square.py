#!/usr/bin/python3

"""square class with a size"""


class Square:
    """"A class Square that defines a square by size"""

    def __init__(self, size=0):
        """Initialize the size with a postive integer"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
