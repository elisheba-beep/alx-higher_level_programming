#!/usr/bin/python3
"""The class MagicClass"""
import math


class MagicClass:
    """an instance of the magic class
    
    Arguments:
       __radius (int): the radius
    """
    def __init__(self, radius=0):
        """initializing the magic class
        
        Args:
            __radius (int): the radius

        Returns:
            None
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
    
    def area(self):
        """Gives the area of the circle
        
        Returns:
            returns the area
        """
        return (self.__radius ** 2) * (math.pi)

    def circumference(self):
        """Gives the circumference of the circle
        
        Returns:
            The circumference of the circle
        """
        return 2 * math.pi * self.__radius