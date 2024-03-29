#!/usr/bin/python3
"""A Function that returns true if object is instance of class"""


def inherits_from(obj, a_class):
    """checking if inherited from specified class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
