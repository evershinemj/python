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
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('The Pie Game - Press 1, 2, 3, 4')
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

# while True:
#     # puts screen.fill(somecolor) inside the while loop
#     # redraws the screen in each iteration with the same
#     # background, thus creating animation effect
#     screen.fill(blue)
#     pygame.display.update()
#     for e in pygame.event.get():
#         if e.type in (QUIT, KEYDOWN):
#             sys.exit()

myfont = pygame.font.Font(None, 60)
color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200
# !!boxes -f $BOXES_SYS_CONF -d whirly -a c
#  .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.
# (                                         )
#  ) # the rectangle containing the circle (
# (                                         )
#  "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"
position = x - radius, y - radius, radius * 2, radius * 2  

piece1 = False
piece2 = False
piece3 = False
piece4 = False

#################################
#         _ ._  _ , _ ._        #
#       (_ ' ( `  )_  .__)      #
#     ( (  (    )   `)  ) _)    #
#    (__ (_   (_ . _) _) ,__)   #
#        `~~`\ ' . /`~~`        #
#        ,::: ;   ; :::,        #
#       ':::::::::::::::'       #
#  _jgs______/_ __ \__________  #
# |                           | #
# | key handling              | #
# |___________________________| #
#################################
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
            elif event.key == pygame.K_2:
                piece2 = True
            elif event.key == pygame.K_3:
                piece3 = True
            elif event.key == pygame.K_4:
                piece4 = True

    screen.fill((0, 0, 200))

# (x, y) is the center of the screen
    textImg1 = myfont.render("1", True, color)
    screen.blit(textImg1, (x + radius / 2 - 20, y - radius / 2))
    textImg2 = myfont.render("2", True, color)
    screen.blit(textImg2, (x - radius / 2, y - radius / 2))
    textImg3 = myfont.render("3", True, color)
    screen.blit(textImg3, (x - radius / 2, y + radius / 2 - 20))
    textImg4 = myfont.render("4", True, color)
    screen.blit(textImg4, (x + radius / 2 - 20, y + radius / 2 - 20))

    if piece1:
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x,y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x,y), (x + radius, y), width)

    if piece2:
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x,y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x,y), (x - radius, y), width)

    if piece3:
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x,y), (x - radius, y), width)
        pygame.draw.line(screen, color, (x,y), (x, y + radius), width)

    if piece4:
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x,y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x,y), (x + radius, y), width)

    if piece1 and piece2 and piece3 and piece4:
        color = 0, 255, 0

    pygame.display.update()

