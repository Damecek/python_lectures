#!/usr/bin/env python3
"""implemets matrix and matrix operations"""


class Matrix:
    def __len__(self):
        return len(self[0])

    def __init__(self, _2Darray):
        self.mat = _2Darray

    def sum(self, _m,):
        return Matrix([[_m[i, j] + self[i, j] for i in range(len(_m))] for j in range(len(self))])


a = Matrix([[1, 2], [4, 7]])
b = Matrix([[4, 3], [1, 2]])
print(a.sum(b))
