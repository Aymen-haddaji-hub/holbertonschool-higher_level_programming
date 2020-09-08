#!/usr/bin/python3
def element_at(my_list, idx):
    a = my_list
    c = idx
    if c < 0 or c > (len(a) - 1):
        return None
    return (a[c])
