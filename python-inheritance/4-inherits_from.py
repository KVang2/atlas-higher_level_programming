#!/usr/bin/python3
"""A Function that returns true if object is instance of class"""


def inherits_from(obj, a_class):
    """checking if inherited from specified class"""
    if isinstance(obj, a_class):
        return isinstance(obj, a_class)
