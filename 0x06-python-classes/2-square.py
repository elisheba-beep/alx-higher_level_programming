#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represents a square
    
    Attributes:
    __size (int): the size of the square side.
    """
    def __init__(self, size=0):
        """Initialize the square
        
        Args:
        size (int): the private size property of the square.

        Returns: None
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size