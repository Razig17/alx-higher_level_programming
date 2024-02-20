#!/usr/bin/python3
"""BaseGeometry class """


class BaseGeometry:
    """"A class named BaseGeometry"""
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Check value if it is a postive integer"""
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
