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
    def __lt__(self, other):
        """Compare if square is less than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size > other.size