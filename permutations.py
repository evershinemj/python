#!/usr/bin/env python3
# encoding=utf-8
from itertools import permutations
l = [1, 2, 3]

if __name__ == '__main__':
    for p in permutations(l):
        print(p)
    print(permutations(l))


