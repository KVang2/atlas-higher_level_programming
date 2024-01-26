#!/usr/bin/python3
"""A Base Class"""

class Base:
"""Base class"""
__nb_objects = 0

def __init__(self, id=None):
    """class attribute"""
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
