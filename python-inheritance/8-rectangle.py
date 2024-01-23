#!/usr/bin/python3
"""Class Rectangle inherits from BaseGeometry"""


class BaseGeometry:
    """Instantiation with width and height"""

    def area(self):
        """Public instance method def area of self"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0")

    def __init__(self, width, height):
        """Instantiation of width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
