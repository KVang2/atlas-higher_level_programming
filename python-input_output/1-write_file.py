#!/usr/bin/python3
""" A function that appends string at the end of a text file"""


def append_write(filename="", text=""):
    """Write a string to UTF8"""

    with open(filename, 'w', encoding='utf-8') as file:
        text_infile = file.write(text)
    return text_infile


if __name__ == "__main__":
    text_infile = write_file("my_first_file.txt", "School is alright!\n")
    print(text_infile)
