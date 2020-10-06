#!/usr/bin/python3
"""base_geometry class"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(Rectangle):
    """
    Square class inherits from Rectangle .
    """
    def __init__(self, size):
        """
        init of the square class
        """
        BaseGeometry.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
