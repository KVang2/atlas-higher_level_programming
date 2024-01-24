#!/usr/bin/python3
""" Function that writes class that inherits from list"""


class MyList(list):
    """define class and printing in sorted order"""

    def print_sorted(self):
        """print elements of list"""
        sorted_list = sorted(self)
        print(sorted_list)
