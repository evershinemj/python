#!/usr/bin/env python3
# encoding: utf-8
#          \\\///
#         / _  _ \
#       (| (.)(.) |)
# .---.OOOo--()--oOOO.--.
# |                     |
# | author: wangxueming |
# | version: 1.0        |
# |                     |
# '--.oooO--------------'
#     (   )   Oooo.
#      \ (    (   )
#       \_)    ) /
#             (_/

import pygame, sys
from pygame.locals import *
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Drawing Arcs')

while True:
    for e in pygame.event.get():
        if e.type in (QUIT, KEYDOWN):
            sys.exit()

    blue = 0, 0, 255
    screen.fill(blue)

    green = 0, 200, 0
    red = 200, 0, 0
    position = 0, 0, 200, 200
    position2 = 200, 200, 300, 100
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    end_angle2 = math.radians(270)
    width = 10
    pygame.draw.arc(screen, green, position, start_angle, end_angle, width)
    pygame.draw.arc(screen, red, position, end_angle, end_angle2, width)
    # pygame.draw.arc(screen, red, position, start_angle, end_angle2, width)
    pygame.draw.arc(screen, green, position2, start_angle, end_angle, width)
    pygame.draw.arc(screen, red, position2, end_angle, end_angle2, width)

    pygame.display.update()
