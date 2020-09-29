#!/usr/bin/python3
"""
square class
"""


class Square:
 """"class"""
    def __init__(self, size=0):
        """init method"""
        self.__size = size

    @property
    def size(self):

        print("retriving size")
        return self.__size

    @size.setter
    def size(self, value):
        """ the size of square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
     """area of square"""
        size = self.__size
        return(size ** 2)
