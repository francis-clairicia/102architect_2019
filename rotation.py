# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## rotation.py
##

from math import cos, sin, radians
from matrix import Matrix

def rotation(mat, d):
    print(f"Rotation by a {d} degree angle")
    d %= 360
    alpha = radians(d)
    matrix_modified = Matrix.unit(3)
    matrix_modified[1, 1] = cos(alpha)
    matrix_modified[1, 2] = -sin(alpha)
    matrix_modified[2, 1] = sin(alpha)
    matrix_modified[2, 2] = cos(alpha)
    matrix_modified *= mat
    return matrix_modified