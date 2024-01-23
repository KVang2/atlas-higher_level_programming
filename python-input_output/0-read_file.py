#!/usr/bin/python3
"""A function that reads a text file and prints to stdout"""


def read_file(filename=""):
    """READ TEXT FILE"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end=""))
