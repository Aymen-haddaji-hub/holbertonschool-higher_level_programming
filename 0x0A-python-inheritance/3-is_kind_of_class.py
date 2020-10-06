#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """
    returns True if object is an instance, or inherits from from a class
    """
    return isinstance(obj, a_class)
