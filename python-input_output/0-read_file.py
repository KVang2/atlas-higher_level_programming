#!/usr/bin/python3
"""A function that reads a text file and prints to stdout"""


def read_file(filename=""):
    """READ TEXT FILE
    args:
        Filename (str): Name of text file.
    Returns:
        None
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
