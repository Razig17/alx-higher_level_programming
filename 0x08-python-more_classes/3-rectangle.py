#!/usr/bin/python3
""""A rectangle class"""


class Rectangle:
    """A class that defines a rectangle by width and height"""

    def __init__(self, width=0, height=0):
        """Initialize the width and height"""
        self.width = width
        self.height = height

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

    def area(self):
        """"Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__height == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a srting with the rectangle with the character #"""

        rec = ""
        if self.__height == 0 or self.__height == 0:
            return (rec)
        for i in range(self.__height):
            for j in range(self.__width):
                rec += "#"
            if (i != (self.__height - 1)):
                rec += "\n"
        return (rec)


my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
