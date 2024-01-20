#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    l_divisible = []
    for i in my_list:
        if i % 2 == 0:
            l_divisible.append(True)
        else:
            l_divisible.append(False)
    return (l_divisible)
