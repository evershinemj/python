#!/usr/bin/env python3
# encoding=utf-8
s1 = 'happy'
s2 = 'funny'
# zip(a, b) creates an iterator that produces a tuple (x, y)
# each time, where x is from sequence a, and y from sequence b
for i, j in zip(s1, s2):  
    print(i, j)
print()
for i in zip(s1, s2):
    print(i)
