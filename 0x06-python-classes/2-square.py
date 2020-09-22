#!/user/bin/python3
"""
This is the Square module.
"""

class Square:
	"""our class"""
    def __init__(self, size=0):
    	"""the init method"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
