#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represents a square
    
    Attributes:
    __size (int): the size of the square side.
    """
    def __init__(self, size):
        """Initialize the square
        
        Args:
        size (int): the private size property of the square.

        Returns: None
        """
        self.__size = size