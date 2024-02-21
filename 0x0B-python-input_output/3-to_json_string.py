#!/usr/bin/python3


"""This module contains to_json_string method"""


from json import dumps


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""

    return dumps(my_obj)
