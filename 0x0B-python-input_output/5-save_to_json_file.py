#!/usr/bin/python3


"""This module contains save_to_json_file method"""


from json import dump


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename, mode="w", encoding="utf-8") as file:
        dump(my_obj, file)
    