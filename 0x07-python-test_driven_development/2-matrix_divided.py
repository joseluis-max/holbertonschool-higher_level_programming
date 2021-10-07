#!/usr/bin/python3
""" Test-driven development
    matrix_divided - Arg:
        matrix: list of list
        div: divided number
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix by a number.
    """
    rel = []
    long = len(matrix[0])
    for i in range(len(matrix)):
        if long != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) in [int, float]:
        if div != 0:
            for item in matrix:
                tmp = []
                for i in item:
                    if type(i) in [int, float]:
                        tmp.append(round(i / div, 2))
                    else:
                        raise TypeError("matrix must be a matrix "
                                        "(list of lists) of integers/floats")
                rel.append(tmp)
        else:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
    return rel
