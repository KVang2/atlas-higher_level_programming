#!/usr/bin/python3
"""Rectangle class that defines area and perimeter"""


class Rectangle:
    """ Defines a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Define property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter, width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise valueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """define height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Checking if height is an integer"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returning area of a Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returning perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
