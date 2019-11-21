# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## scaling.py
##

from matrix import Matrix

def scaling(mat, m, n):
    print(f"Scaling by factor {m} and {n}")
    matrix_modified = Matrix.unit(3)
    matrix_modified[1, 1] = m
    matrix_modified[2, 2] = n
    matrix_modified *= mat
    return matrix_modified