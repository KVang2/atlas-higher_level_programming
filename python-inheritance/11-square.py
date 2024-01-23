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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Defines class Rectangle that inherits from  BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation of width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method implemented returning area"""
        return self.__width * self.__height

    def __str__(self):
        """Returning string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class square inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def _str__(self):
        """Method that returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
