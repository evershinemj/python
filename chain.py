#!/usr/bin/env python3
# encoding=utf-8
from itertools import chain
s1 = 'night'
s2 = 'sound'
for i in chain(s1, s2):
    print(i)
