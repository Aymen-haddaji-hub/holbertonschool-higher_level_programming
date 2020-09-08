#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    edited_list = my_list[:]
    if idx < 0 or idx > (a +1):
        return edited_list
    edited_list[idx] = element
    return edited_list
