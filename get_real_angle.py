# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## get_real_angle.py
##

def get_real_angle(angle):
    while (angle >= 360):
        angle -= 360
    while (angle <= -360):
        angle += 360
    return angle