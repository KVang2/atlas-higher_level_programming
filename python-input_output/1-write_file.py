#!/usr/bin/python3
""" A function that appends string at the end of a text file"""


def append_write(filename="", text=""):
    """Write a string to UTF8"""

    with open(filename) as file:
        for line in file:
            line += 1
    return
