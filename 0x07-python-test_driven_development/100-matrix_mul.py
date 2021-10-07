#!/usr/bin/python3
"""Multiplies 2 matrices
"""


def can_multiplied(m1, m2):
    """
    Check if matrix's can to be multiplied
        Args:
            m1: matrix
            m2: matrix
    """
    n_col_m1 = len(m1[0])
    n_row_m2 = len(m2)
    if n_col_m1 == n_row_m2:
        return True
    else:
        return False


def is_same_size(matrix):
    """
    Check if row matrix have the same size
        Args:
            matrix: list
    """
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            return False
    return True


def is_int_or_float(matrix):
    """
    Check if matrix have only int and float
        Args:
            matrix: list
    """
    for row in matrix:
        for col in row:
            if type(col) not in [int, float]:
                return False
    return True


def is_empty(matrix):
    """
    Check if matrix is Empty
        Args:
            matrix: list
    """
    if len(matrix) == 0:
        return True
    else:
        for item in matrix:
            if len(item) == 0:
                return True
    return False


def is_list_of_lists(matrix):
    """
    Check if matrix is a list of lists
        Args:
            matrix: list
    """
    for item in matrix:
        if type(item) is not list:
            return False
    return True


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices
        Arg:
            m_a: list of lists with int or floats
            m_b: list of lists with int of floats
    """
    if type(m_a) is list:
        if type(m_b) is list:
            if is_list_of_lists(m_a):
                if is_list_of_lists(m_b):
                    if not is_empty(m_a):
                        if not is_empty(m_b):
                            if is_int_or_float(m_a):
                                if is_int_or_float(m_b):
                                    if is_same_size(m_a):
                                        if is_same_size(m_b):
                                            if can_multiplied(m_a, m_b):
                                                rel = []
                                                for i in range(len(m_a)):
                                                    tmp_l = []
                                                    for j in range(len(m_b[0])):
                                                        tmp_n = 0
                                                        for k in range(len(m_b)):
                                                            tmp_n += m_a[i][k] * m_b[k][j]
                                                        tmp_l.append(tmp_n)
                                                    rel.append(tmp_l)
                                                return rel
                                            else:
                                                raise ValueError("m_a and m_b can't be multiplied")
                                        else:
                                            raise TypeError("each row of m_b must be of the same size")
                                    else:
                                        raise TypeError("each row of m_a must be of the same size")
                                else:
                                    raise TypeError("m_b should contain only integers or floats")
                            else:
                                raise TypeError("m_a should contain only integers or floats")
                        else:
                            raise ValueError("m_b can't be empty")
                    else:
                        raise ValueError("m_a can't be empty")
                else:
                    raise TypeError("m_b must be a list of lists")
            else:
                raise TypeError("m_a must be a list of lists")
        else:
            raise TypeError("m_b must be a list")
    else:
        raise TypeError("m_a must be a list")
