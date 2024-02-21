#!/usr/bin/python3


"""This module contains from_json_string method"""


from json import loads


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""

    return loads(my_str)
