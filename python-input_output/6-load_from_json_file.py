#!/usr/bin/python3
"""Function that creates an Object from JSON file"""
import json


def load_from_json_file(filename):
    """Open load from json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
