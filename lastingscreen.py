#!/usr/bin/env python3
# encoding=utf-8
import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))

# None means default font
# it's just a way of implementation
myfont = pygame.font.Font(None, 60)
white = 255, 255, 255
blue = 0, 0, 255
# True means the value of antialias is True
# Having it as a parameter is just a way of image
text = myfont.render("Hey, pygame", True, white)
screen.fill(blue)
screen.blit(text, (100, 100))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
