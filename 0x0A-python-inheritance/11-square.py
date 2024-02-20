#!/usr/bin/python3


"""A module contains "Square" class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize size"""

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ return the sqaure description"""

        return f"[Square] {self.__size}/{self.__size}"
    def area(self):
        """Returns the area of the square"""

        return self.__size * self.__size
