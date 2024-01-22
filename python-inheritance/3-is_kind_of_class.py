#!/usr/bin/python3
"""A function that returns instance of a class"""


def is_kind_of_class(obj, a_class):
    """Instance of a class that inherited from the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
