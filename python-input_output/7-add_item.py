#!/usr/bin/python3
"""A script that adds all arguments to a python list, then save"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """Saving json file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Open load from json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


filename = 'add_item.json'


try:
    my_list = load_from_json_file(filename)
except Exception as e:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)
