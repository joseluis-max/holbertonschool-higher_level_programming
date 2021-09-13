#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = 0
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > _max:
            _max = i
    return _max
