#!/usr/bin/python3
"""Integer validator, class BaseGeometry"""


class BaseGeometry:
    """Public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validator Value is an int"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
