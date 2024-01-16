#!/usr/bin/python3
"""A function that prints Name"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not instance(last_name, str):
        raise TypeError("first_name must be a string, and last_name must be a string
        print(f"My name is {first_name} {last_name}")
