# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## rotation.py
##

import math
from get_real_angle import get_real_angle
from matrix import unit_matrix

def rotation(mat, d):
    print(f"Rotation by a {d} degree angle")
    d = math.radians(get_real_angle(d))
    matrix_modif = unit_matrix(3)
    matrix_modif[1, 1] = math.cos(d)
    matrix_modif[1, 2] = -math.sin(d)
    matrix_modif[2, 1] = math.sin(d)
    matrix_modif[2, 2] = math.cos(d)
    return matrix_modif * mat