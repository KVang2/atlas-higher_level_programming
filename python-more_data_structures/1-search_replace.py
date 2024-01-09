#!/usr/bin/python3
def search_replace(my_list, search, replace):
    initial_list = list(my_list)
    for i in range(len(initial_list)):
        if initial_list[i] == search:
            initial_list[i] = replace
    return initial_list
