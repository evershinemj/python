#!/usr/bin/env python3
# encoding=utf-8
from itertools import zip_longest

t1 = (1, 2, 3)
t2 = (1, 4, 9, 16)
print('calling zip(t1, t2)')
for i, j in zip(t1, t2):
    print(i , j, sep = ' : ')
print()
print('calling zip_longest(t1, t2)')
for i, j in zip_longest(t1, t2):
    print(i , j, sep = ' : ')
print()
print('calling zip_longest(t1, t2, fillvalue = "nothing")')
for i, j in zip_longest(t1, t2, fillvalue = "nothing"):
    print(i , j, sep = ' : ')
