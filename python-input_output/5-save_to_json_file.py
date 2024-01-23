#!/usr/bin/python3
"""Function that writes an Object to text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        file.write(json_obj)
