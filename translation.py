##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## translation.py
##

from matrix import unit_matrix

def translation(mat, i, j):
    print(f"Translation along vector ({i}, {j})")
    matrix_modif = unit_matrix(3)
    matrix_modif[1, 3] = i
    matrix_modif[2, 3] = j
    return matrix_modif * mat