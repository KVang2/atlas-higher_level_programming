#!/usr/bin/python3
"""Function that prints a text with 2 new lines"""


def text_indentation(text):
    """checking if its a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    text = '\n'.join(line.strip() for line in text.split('\n'))
    print(text)
