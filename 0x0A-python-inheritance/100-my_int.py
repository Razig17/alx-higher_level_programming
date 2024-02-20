#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """ Class Myint has == and != operators inverted"""
    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
