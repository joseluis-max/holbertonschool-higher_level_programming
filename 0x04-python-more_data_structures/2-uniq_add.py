#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_list = list(set(my_list))
    sum = 0
    for item in n_list:
        sum = sum + item
    return sum
