#!/usr/bin/python3
"""Rectangle How Many Instances"""


class Rectangle:
    """ Defines a Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """String of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Method of returning a string"""
        return "Rectangle([], [])".format(self.__width, self.__height)

    def __del__(self):
        """Method of printing a message after deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
