#!/usr/bin/python3

"""This module contains append_after method"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file
    after each line containing a specific string
    """

    lns = ""
    with open(filename, mode="r", encoding="UTF8") as file:
        for ln in file:
            if search_string in ln:
                ln += new_string
        lns += ln

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(lns)
