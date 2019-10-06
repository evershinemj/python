#!/usr/bin/env python3
# encoding=utf-8
import math
from functools import partial
from distance import distance

p = partial(distance, (0, 0))
l = [(5, 10), (1, 3), (2, 2), (0, 4)]
l.sort(key = p)

if __name__ == '__main__':
    print(l)
