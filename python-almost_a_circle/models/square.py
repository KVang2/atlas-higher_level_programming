#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""


class Square(Rectangle):
    """Class Sqaure attribute"""
    def __init__(self, size, x=0, y=0, id=None):
        """calling super class"""
        super().__init__(id, size, size, x, y)
    
    def __str__(self):
        return "[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
