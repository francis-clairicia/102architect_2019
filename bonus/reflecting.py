# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## reflecting.py
##

from math import cos, sin, radians
from matrix import Matrix

def reflecting(mat, d):
    print(f"Reflection over an axis with an inclination angle of {d} degrees")
    d = radians(d)
    matrix_transformation = Matrix.identity(3)
    matrix_transformation[1, 1] = cos(2 * d) if d != 0 else 1
    matrix_transformation[1, 2] = sin(2 * d)
    matrix_transformation[2, 1] = sin(2 * d)
    matrix_transformation[2, 2] = -cos(2 * d) if d != 0 else 1
    return matrix_transformation * mat
