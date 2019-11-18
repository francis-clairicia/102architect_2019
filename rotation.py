##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## rotation.py
##

import math
from get_real_angle import get_real_angle

def rotation(x, y, d):
    print(f"Rotation by a {d} degree angle")
    d = get_real_angle(d)
    radius = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    angle = math.asin(y / radius)
    angle += 2 * math.pi if angle < 0 else 0
    angle += math.radians(d)
    x = math.cos(angle) * radius
    y = math.sin(angle) * radius
    x = 0 if x == 0 else x
    y = 0 if y == 0 else y
    return (x, y)