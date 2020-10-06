#!/usr/bin/python3
"""Check if the object is an instance of class """


def is_same_class(obj, a_class):
    """ Check True if the object is exactly an instance of the specified class ; otherwise False """
    return type(obj) == a_class
