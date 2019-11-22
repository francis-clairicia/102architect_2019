# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## scaling.py
##

from matrix import Matrix

def scaling(mat, m, n):
    print(f"Scaling by factors {m} and {n}")
    matrix_transformation = Matrix.unit(3)
    matrix_transformation[1, 1] = m
    matrix_transformation[2, 2] = n
    return matrix_transformation * mat