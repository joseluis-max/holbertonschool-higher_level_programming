#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = [];
    square = lambda x : x * x
    for i in matrix:
        n_matrix.append(list(map(square, i)))
    return n_matrix
