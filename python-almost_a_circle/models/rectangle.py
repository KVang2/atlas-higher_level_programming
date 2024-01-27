#!/usr/bin/python3
"""A class Rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
    """Class Rectangle Private instance attributes"""

def __init__(self, width, height, x=0, y=0, id=None):
    """Attribute of width height"""
    super().__init__(id)
    self.width = width
    self.height = height
    self.x = x
    self.y = y

@property
def width(self):
    """Getter for width"""
    return self.__width

@width.setter
def width(self, value):
    """Setter for width"""
    self.__width = value

@property
def height(self):
    """Getter height"""
    return self.__height

@height.setter
def height(self, value):
    """Setter height"""
    self.__height = value

@property
def y(self):
    """y Getter"""
    return self.__y

@y.setter
def y(self, value):
    """y setter"""
    self.__y = value