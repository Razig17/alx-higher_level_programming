#!/usr/bin/python3

""""A rectangle class"""


class Rectangle:
    """A class that defines a rectangle by width and height"""

    def __init__(self, width=0, height=0):
        """Initialize the width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """"Retrieves the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """"Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """"Retrieves the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """"Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
