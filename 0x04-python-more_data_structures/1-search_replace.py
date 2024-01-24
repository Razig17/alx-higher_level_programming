#!/usr/bin/python3

def search_replace(my_list, search, replace):

    replaced = []
    for i in my_list:
        if i == search:
            replaced.append(replace)
        else:
            replaced.append(i)
    return replaced
