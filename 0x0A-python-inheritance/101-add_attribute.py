#!/usr/bin/python3


"""A module contains "Square" class"""


def add_attribute(obj, attribute_name, attribute_value):
    """Adds a new attribute to an object if its possible"""

    if not hasattr(obj, '__dict__') or hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute_name, attribute_value)
