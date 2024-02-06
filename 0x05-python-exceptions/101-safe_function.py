#!/usr/bin/python3

def safe_function(fct, *args):

    from sys import stderr
    try:
        a = fct(args)
        return (a)
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
        return (None)
