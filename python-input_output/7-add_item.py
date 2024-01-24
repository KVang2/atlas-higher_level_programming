#!/usr/bin/python3
"""A script that adds all arguments to a python list, then save"""
import sys
from save_to_json_file = import ('5-save_to_json_file').save_to_json_file
from load_from_json_file = import ('6-load_from_json_file')

filename = 'add_item.json'
my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_lists, filename)
