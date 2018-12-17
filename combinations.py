#!/usr/bin/env python3
# encoding=utf-8
from itertools import combinations

l = [1, 2, 3]

if __name__ == '__main__':
    for c in combinations(l, 2):  # two positional args
        print(c)
    print(combinations(l, 2))
