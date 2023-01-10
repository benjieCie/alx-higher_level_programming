#!/usr/bin/python3
""" A function that returns a list of lists of integers
representing the Pascal’s triangle"""


def pascal_triangle(n):
    """Function that returns a list of lists of ints
    representing the pascals triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        a = triangle[-1]
        tmp = [1]
        for i in range(len(a) - 1):
            tmp.append(a[i] + tri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
