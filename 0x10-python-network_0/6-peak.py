#!/usr/bin/python3
"""
This module contain a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers is None:
        return None
    else:
        list_of_integers.sort()
        return list_of_integers[-1]
