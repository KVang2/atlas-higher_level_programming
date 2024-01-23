#!/usr/bin/python3
""" A function that appends string at the end of a text file"""


def append_write(filename="", text=""):
    """Write a string to UTF8"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
