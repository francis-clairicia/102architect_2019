# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## reflecting.py
##

import math
from get_real_angle import get_real_angle

def reflecting(x, y, d):
    print(f"Reflection over an axis with an inclination angle of {d} degrees")
    d = math.radians(get_real_angle(d))
    radius = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    if (y >= 0):
        alpha_angle = math.asin(y / radius)
    else:
        alpha_angle = math.asin(y / radius) + (2 * math.pi)
    if (d - math.pi >= alpha_angle):
        d -= math.pi
    angle = 2 * d - alpha_angle
    x = math.cos(angle) * radius
    y = math.sin(angle) * radius
    x = 0 if x == 0 else x
    y = 0 if y == 0 else y
    return (x, y)