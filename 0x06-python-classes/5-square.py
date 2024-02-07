#!/usr/bin/python3
"""square class"""


class Square:
    """"A class Square that defines a square by size"""

    def __init__(self, size=0):
        """Initialize the size"""
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square"""
        print("start")
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """Retrieves the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """"Sets the size value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
