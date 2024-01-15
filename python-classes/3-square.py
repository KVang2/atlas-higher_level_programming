#!/usr/bin/python3
"""Area of a square"""


class Square:
    """objective"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """area of square"""
    def area(self):
        return self.__size ** 2
