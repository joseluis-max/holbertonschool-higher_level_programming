#!/usr/bin/python3
""" Inherance """


def inherits_from(obj, a_class):
    """ Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False."""

    return type(obj) != a_class and isinstance(obj, a_class)
