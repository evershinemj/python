#!/usr/bin/env python3
# encoding=utf-8
import pygame, sys
from pygame.locals import *

pygame.init()
# type of screen is Surface
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Drawing Circles')
blue = 0, 0, 255
screen.fill(blue)
# cirle(screen, color, pos, radius, width=0)
color = 255, 0, 0
pos = 300, 200
radius = 100
width = 10
pygame.draw.circle(screen, color, pos, radius, width)
pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type in (QUIT, KEYDOWN):
            sys.exit()

