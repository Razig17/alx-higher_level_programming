#!/usr/bin/python3

""""This module contains a function thet adds two integers"""


def add_integer(a, b=98):
    """"Adds 2 integers"""

    if not isinstance(a, (int, float)):
        raise ValueError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise ValueError('b must be an integer')
    return (int(a) + int(b))
