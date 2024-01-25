#!/usr/bin/python3
""" A function that appends string at the end of a text file"""


def write_file(filename="", text=""):
    """Write a string to UTF8
    Args:
        filename: Name of file

    Returns:
        written characters
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
