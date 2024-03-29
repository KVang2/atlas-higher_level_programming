#!/usr/bin/python3
"""A function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """String at the end of file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
