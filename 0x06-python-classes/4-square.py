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

        Returns:
            None
        """
        self.__size = size

    @property
    def size(self):
        """gets the size property
        
        Returns:
            returns the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size of the square
        
        Args:
            value (int): the value which is to be set.

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value



    def area(self):
        """Calculates the area of the square
        
        Returns:
            returns the area of the square
        """
        return self.__size * self.__size