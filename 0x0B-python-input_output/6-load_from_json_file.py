#!/usr/bin/python3


"""This module contains load_from_json_file method"""


from json import load


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="UTF8") as file:
        obj = load(file)
    return obj
