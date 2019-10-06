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

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Drawing Lines')

while True:
    screen.fill((0, 255, 0))
    color = 200, 0, 0
    start = (0, 0)
    end = (400, 300)
    # set width to 0 makes the line invisible
    # width = 0
    width = 10
    pygame.draw.line(screen, color, start, end, width)
    pygame.display.update()
    for e in pygame.event.get():
        if e.type in (QUIT, KEYDOWN):
            sys.exit()
