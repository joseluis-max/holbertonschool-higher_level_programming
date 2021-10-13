#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    pt = [[1]]
    trow = [1]
    y = [0]
    for x in range(n - 1):
        trow = [left + right for left, right in zip(trow + y, y + trow)]
        pt.append(trow)
    return pt
