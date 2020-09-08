#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    list.sort(my_list, reverse=True, key=int)
    return my_list[0]
