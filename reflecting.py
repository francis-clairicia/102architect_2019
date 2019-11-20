# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## reflecting.py
##

import math
from matrix import unit_matrix
from get_real_angle import get_real_angle

def reflecting(mat, d):
    print(f"Reflection over an axis with an inclination angle of {d} degrees")
    d = math.radians(get_real_angle(d))
    matrix_modif = unit_matrix(3)
    matrix_modif[1, 1] = math.cos(2 * d) if d != 0 else 1
    matrix_modif[1, 2] = math.sin(2 * d)
    matrix_modif[2, 1] = math.sin(2 * d)
    matrix_modif[2, 2] = -math.cos(2 * d) if d != 0 else 1
    return matrix_modif * mat