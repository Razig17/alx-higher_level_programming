#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    len_a, len_b = len(tuple_a), len(tuple_b)
    n, m = 0, 0
    if len_a >= 1:
        n += tuple_a[0]
    if len_b >= 1:
        n += tuple_b[0]
    if len_a >= 2:
        m += tuple_a[1]
    if len_b >= 2:
        m += tuple_b[1]
    return ((n, m))
