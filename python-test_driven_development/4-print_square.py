#!/usr/bin/python3
"""Print square size"""


def print_square(size):
   """square size"""
   if not isinstance(size, int):
            raise TypeError("size must be an integer")
   if size < 0:
            raise ValueError("size must be >= 0")
   if isinstance(size, float) and size < 0:
            raise ValueError("size must be an integer")
   for i in range(size):
            print(f"#" * size)
