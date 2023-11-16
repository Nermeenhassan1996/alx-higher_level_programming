#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp = []
    tmp.append(list(map(lambda x: x**2, matrix)))
    return (tmp)
