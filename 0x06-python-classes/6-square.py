#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represents a square
    
    Attributes:
        __size (int): the size of the square side.
    """
    def __init__(self, size=0, position=(0,0)):
        """Initialize the square
        
        Args:
            size (int): the private size property of the square.
            position (tuple): a tuple with two positive integers

        Returns:
            None
        """
        self.__size = size
        self.__position = position

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


    @property
    def position(self):
        """gets the position property
        
        Returns:
            returns the position
        """
        return self.__position

    @size.setter
    def position(self, value):
        """Sets the value of the position of the square
        
        Args:
            value (tuple): the value which is to be set.

        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int \
            or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value



    def area(self):
        """Calculates the area of the square
        
        Returns:
            returns the area of the square
        """
        return self.__size * self.__size
    
    def my_print(self):
        """Prints the square using the # symbol
        
        Returns:
            None
        """
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
        if self.__size == 0:
            print()