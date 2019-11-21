##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## translation.py
##

from matrix import Matrix

def translation(mat, i, j):
    print(f"Translation along vector ({i}, {j})")
    matrix_modified = Matrix.unit(3)
    matrix_modified[1, 3] = i
    matrix_modified[2, 3] = j
    return matrix_modified * mat