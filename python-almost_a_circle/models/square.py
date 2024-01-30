#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Sqaure attribute"""
    def __init__(self, size, x=0, y=0, id=None):
        """calling super class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str def"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
