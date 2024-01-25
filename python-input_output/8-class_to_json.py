#!/usr/bin/python3
"""A function that returns dictionary description with simple data structre"""


def class_to_json(obj):
    """Returns simple data structure"""
    return obj.__dict__
