#!/usr/bin/python3

"""This module contains "Square" class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}"

    @property
    def size(self):
        """Retrieves the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attattributes """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        return {
                "id": self.id,
                'size': self.width,
                "x": self.x,
                "y": self.y
        }
