#!/usr/bin/python3
"""Function that prints a text with 2 new lines"""


def text_indentation(text):
    """checking if its a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    space = ""
    for char in text:
        space += char
        if char in ['.', '?', ':']:
            print(space)
