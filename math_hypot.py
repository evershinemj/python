#!/usr/bin/env python3
# encoding=utf-8
import math

x = 5
y = 12
# get the hypotenuse
hypot = math.hypot(x, y)
# using string formatting is more elegant than
# concatenating string with '+' when there are
# multiple args
print('x: %d, y: %d' % (x, y))
print('calling math.hypot(x, y)')
print(hypot)
x = 7
y = 24
hypot = math.hypot(x, y)
print('x: %d, y: %d' % (x, y))
print('calling math.hypot(x, y)')
print(hypot)
