#!/usr/bin/python3
"""A function that returns True if object is the same as the specified class"""


def is_same_class(obj, a_class):
    """ if type obj is class return true if not false"""
    if type(obj) is a_class:
        return True
    else:
        return False
