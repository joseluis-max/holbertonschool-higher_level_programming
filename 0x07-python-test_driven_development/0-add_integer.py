#!/usr/bin/python3
""" Test-driven development
    Add_integer - Arg:
        a: int or float number
        b: int or float number
"""


def add_integer(a, b=98):
    """
    Return sum of two integers
    """

    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            if a == a + 1:
                raise OverflowError("a is too large")
            a = int(a)
            if b == b + 1:
                raise OverflowError("b is too large")
            b = int(b)
            return a + b
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
