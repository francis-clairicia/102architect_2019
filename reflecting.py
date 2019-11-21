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
    d = radians(d % 360)
    matrix_modified = Matrix.unit(3)
    matrix_modified[1, 1] = cos(2 * d) if d != 0 else 1
    matrix_modified[1, 2] = sin(2 * d)
    matrix_modified[2, 1] = sin(2 * d)
    matrix_modified[2, 2] = -cos(2 * d) if d != 0 else 1
    return matrix_modified * mat