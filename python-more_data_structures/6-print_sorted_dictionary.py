#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary)
    for i in sort_keys:
        print(f"{i}: {a_dictionary[i]}")
