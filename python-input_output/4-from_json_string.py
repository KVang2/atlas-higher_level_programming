#!/usr/bin/python3
"""Function that returns an object"""
import json


def from_json_string(my_str):
    """Returning object by JSON string"""
    return json.loads(my_str)
