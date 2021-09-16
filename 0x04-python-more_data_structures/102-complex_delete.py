#!/usr/bin/python3
def complex_delete(a_dictionary, value):
        while value in a_dictionary.values():
                a_dictionary.pop(list(a_dictionary.keys())[list(a_dictionary.values()).index(value)])
        return a_dictionary
