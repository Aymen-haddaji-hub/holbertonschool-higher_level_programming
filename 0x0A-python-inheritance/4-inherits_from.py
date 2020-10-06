#!/usr/bin/python3
""" inherits_from Module"""


def inherits_from(obj, a_class):
    """
    Check and Return True if he object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
