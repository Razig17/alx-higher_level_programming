#!/usr/bin/python3

"""square class"""


class Square:
    """"A class Square that defines a square by size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size and position"""
        self.size = size
        self.position = position

    def __str__(self):
        """A method to print square when using print"""

        pos = ""
        if self.size == 0:
            return ""
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos[:-1]

    @property
    def size(self):
        """Retrieves the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """"Sets the size value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Retriieves the position"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position"""

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
