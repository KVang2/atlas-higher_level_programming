#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """objective"""
    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """area def"""
    def area(self):
        return self.__size ** 2

    """ size"""
    def size(self):
        return self.__size

    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
