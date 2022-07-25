#!/usr/bin/python3
"""The rectangle class"""


class Rectangle:
    """Defines a rectangle
    
    Attributes:
    __width (int):
        The width of the rectangle
    __height (int):
        The height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """The initialised rectangle
        
        Args:
        width (int):
            the width of the rectangle
        height (int):
            the height of the rectangle
        
        Returns:
            None
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """Gets the width value
        
        returns:
            the width
        """
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the width value
        
        Args:
        value(int):
            the value to be set

        Returns:
            the set value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        """Gets the height value
        
        Returns:
            the height
        """
        return self.__height
    @height.setter
    def height(self, value):
        """Sets the height value
        
        Args:
        value(int):
            the value to be set

        Returns:
            the set height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
        
    def area(self):
        """gives the rectangle area
        
        Returns:
            the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """gives the perimeter of a rectangle
        
        Returns:
            the calculated perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)