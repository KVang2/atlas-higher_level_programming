#!/usr/bin/python3
""" Function that writes class that inherits from list"""


class MyList(list):
    """define class and printing in sorted order"""
    def __init__(self, int_list):
        super().__init__(int_list)

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
