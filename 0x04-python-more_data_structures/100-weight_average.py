#!/usr/bin/python3

def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0
    div = 0
    average = 0
    for i, v in my_list:
        average += i * v
        div += v
    average = average / div
    return average
