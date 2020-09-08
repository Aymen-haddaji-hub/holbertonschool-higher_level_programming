#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    edited_list = my_list[:]
    if idx < 0 or idx > len(my_list):
        return edited_list
    edited_list[idx] = element
    return edited_list
