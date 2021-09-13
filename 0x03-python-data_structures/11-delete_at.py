#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or len(my_list) <= idx:
        return my_list
    _list = my_list[:idx] + my_list[idx + 1, :]
    return _list
