# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## scaling.py
##

from matrix import unit_matrix

def scaling(mat, m, n):
    print(f"Scaling by factor {m} and {n}")
    matrix_modif = unit_matrix(3)
    matrix_modif[1, 1] = m
    matrix_modif[2, 2] = n
    return matrix_modif * mat