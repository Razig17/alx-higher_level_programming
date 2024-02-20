#!/usr/bin/python3
"""
This module contains a function that
finds is an object is an instance of a subclass of a given class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class  otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
