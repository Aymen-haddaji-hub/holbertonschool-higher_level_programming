#!/usr/bin/python3
""" base_geometry Module """


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """ area method """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ public method that validate value
        name : is string
        if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
