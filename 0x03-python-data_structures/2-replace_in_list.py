#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    a = my_list
    c = idx
    if c >= 0 and c < len(a):
        a[c] = element
    return (a)
