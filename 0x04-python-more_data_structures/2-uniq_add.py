#!/usr/bin/python3
import functools


def uniq_add(my_list=[]):
    n_list = functools.reduce(lambda a, b: a + b, set(my_list))
    return n_list
