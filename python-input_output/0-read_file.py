#!/usr/bin/python3
"""A function that reads a text file and prints to stdout"""


def read_file(filename=""):
    """READ TEXT FILE"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(line, end='')

if __name__ == "__main__":
    read_file("my_file_o.txt")
