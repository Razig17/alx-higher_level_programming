#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sorted_dir = dict(sorted(a_dictionary.items()))
    for i, j in sorted_dir.items():
        print("{}: {}".format(i, j))
