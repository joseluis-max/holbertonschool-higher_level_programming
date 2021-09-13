#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) <= idx:
        return my_list.copy()
    copy = my_list.copy()
    copy[idx] = element
    return copy
