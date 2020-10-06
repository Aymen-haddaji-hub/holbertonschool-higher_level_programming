#!/usr/bin/python3
"""base_geometry class"""


class BaseGeometry:
    """
    base_geometry class
    """
    def area(self):
        """
        returns the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle the class
    """
    def __init__(self, width, height):
        """
        the init of the class
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        return a string
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """
        the area of a rectangle
        """
        return self.__width * self.__height
