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
    d = radians(d % 360)
    matrix_modified = Matrix.unit(3)
    matrix_modified[1, 1] = cos(d)
    matrix_modified[1, 2] = -sin(d)
    matrix_modified[2, 1] = sin(d)
    matrix_modified[2, 2] = cos(d)
    return matrix_modified * mat