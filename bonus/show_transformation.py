# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## show_transformation.py
##

import pygame
from translation import translation
from scaling import scaling
from rotation import rotation
from reflecting import reflecting

TREATEMENT = {
    "-t": translation,
    "-z": scaling,
    "-r": rotation,
    "-s": reflecting
}

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 155, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def draw_axis(window, origin, unit):
    window_rect = window.get_rect()
    abscissa = [
        [window_rect.left, origin[1]],
        origin,
        [window_rect.right, origin[1]]
    ]
    ordinate = [
        [origin[0], window_rect.top],
        origin,
        [origin[0], window_rect.bottom]
    ]
    graduate_size = 15
    pygame.draw.lines(window, BLACK, False, abscissa, 2)
    point = 0
    while origin[0] + (point * unit) < window_rect.right:
        point += 1
        graduate = [
            [origin[0] + (point * unit), origin[1] - (graduate_size // 2)],
            [origin[0] + (point * unit), origin[1] + (graduate_size // 2)]
        ]
        pygame.draw.line(window, BLACK, graduate[0], graduate[1], 2)
    point = 0
    while origin[0] + (point * unit) > window_rect.left:
        point -= 1
        graduate = [
            [origin[0] + (point * unit), origin[1] - (graduate_size // 2)],
            [origin[0] + (point * unit), origin[1] + (graduate_size // 2)]
        ]
        pygame.draw.line(window, BLACK, graduate[0], graduate[1], 2)
    pygame.draw.lines(window, BLACK, False, ordinate, 2)
    point = 0
    while origin[1] + (point * unit) > window_rect.top:
        point -= 1
        graduate = [
            [origin[0] - (graduate_size // 2), origin[1] + (point * unit)],
            [origin[0] + (graduate_size // 2), origin[1] + (point * unit)]
        ]
        pygame.draw.line(window, BLACK, graduate[0], graduate[1], 2)
    while origin[1] + (point * unit) < window_rect.bottom:
        point += 1
        graduate = [
            [origin[0] - (graduate_size // 2), origin[1] + (point * unit)],
            [origin[0] + (graduate_size // 2), origin[1] + (point * unit)]
        ]
        pygame.draw.line(window, BLACK, graduate[0], graduate[1], 2)
    point = 0

def get_transformations(point, flags):
    points = list()
    last_point = point
    for flag, args in flags:
        first_point = last_point
        last_point = TREATEMENT[flag](first_point, *args)
        points.append((first_point, last_point))
    return points

def draw_transformations(window, origin, unit, points):
    for k in range(2):
        for point_list in points:
            p_l = point_list
            point = [(origin[0] + (p[1, 1] * unit), origin[1] - (p[2, 1] * unit)) for p in p_l]
            point = [(int(p[0]), int(p[1])) for p in point]
            if not k:
                pygame.draw.lines(window, ORANGE, False, point)
            else:
                pygame.draw.circle(window, RED, point[0], 10)
    pygame.draw.circle(window, BLUE, point[1], 10)

def show_transformation(point, flags):
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("102architect")
    clock = pygame.time.Clock()
    points = get_transformations(point, flags)
    done = False
    origin = [400, 300]
    unit = 50
    while not done:
        clock.tick(30)
        window.fill(WHITE)
        draw_axis(window, origin, unit)
        draw_transformations(window, origin, unit, points)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                origin[0] += event.rel[0]
                origin[1] += event.rel[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                unit += 3 * (event.button == 4) - 3 * (event.button == 5)
    pygame.quit()
