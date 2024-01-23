#!/usr/bin/python3
""" A function that appends string at the end of a text file"""


def append_write(filename="", text=""):
    """Write a string to UTF8
    Args:
        filename, to write.
        text (str): The text that is written in the file
    Returns:
        Number of characters
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
