#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """objective"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must not be an integer")
        elif value < 0:
            raise ValueError("size must be >- 0")
        self.__size = value

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all (i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            for i in range(self.__size):
                print(" " * self.__size * ( i > 0), end="")
                print("#" * self.__size)
        
