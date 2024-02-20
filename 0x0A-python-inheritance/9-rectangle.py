#!/usr/bin/python3


"""A module contains "Rectangle" class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize an instance with only positive integer parameters"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ return, the rectangle description"""

        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height
