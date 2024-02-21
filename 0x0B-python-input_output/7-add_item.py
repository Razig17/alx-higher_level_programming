#!/usr/bin/python3

"""
This module contains a script that adds all arguments to a list,
and then save them to a file as json representation
"""

from sys import argv
from json import load
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = argv [1:]

try:
    args_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    args_list = []

for arg in args:
    args_list.append(arg)

save_to_json_file(args_list, "add_item.json")
