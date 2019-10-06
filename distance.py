#!/usr/bin/env python3
# encoding=utf-8
import math


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    # impl of math.hypot(x, y):
    # math.sqrt(x * x + y * y)
    return math.hypot(x1 - x2, y1 - y2)


if __name__ == '__main__':
    d = distance((1, 1), (-1, -1))
    print(d)
