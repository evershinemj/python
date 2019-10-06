#!/usr/bin/env python3
# encoding=utf-8
import pygame, sys
from pygame.locals import *

pygame.init()
# type of screen is Surface
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Drawing Rectangles')
pos_x = 300
pos_y = 200
vel_x = 2
vel_y = 1
# screen.fill((0, 0, 200))

while True:
    # screen.fill should be in the while loop
    # otherwise the trace of rectangles moving
    # will be retained
    screen.fill((0, 0, 200))
    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 300 or pos_y < 0:
        vel_y = -vel_y

    color = 255, 0, 0
    width = 0 
    pos = pos_x, pos_y, 100, 100
# rect(Surface, color, Rect, width=0) -> Rect
    pygame.draw.rect(screen, color, pos, width)
    #                         \\\///
    #                        / _  _ \
    #                      (| (.)(.) |)
    # .------------------.OOOo--()--oOOO.------------------.
    # |                                                    |
    # | # in the way several display changes can be cached |
    # | # and screen will be updated only when you want    |
    # |                                                    |
    # '------------------.oooO-----------------------------'
    #                     (   )   Oooo.
    #                      \ (    (   )
    #                       \_)    ) /
    #                             (_/
    pygame.display.update()

    for e in pygame.event.get():
        if e.type in (QUIT, KEYDOWN):
            sys.exit()

# vim: set iskeyword-=- :
