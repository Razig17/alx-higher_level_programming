#!/usr/bin/python3


"""This module contains Read_file method"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode="r",encoding="utf-8") as file:
        lines = file.read()
    print(lines, end="")
