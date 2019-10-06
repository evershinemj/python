#!/usr/bin/env python3
# encoding=utf-8

x = 5
addx = lambda y, x = x : x + y
x = 10
addx2 = lambda y, x = x : x + y

if __name__ == '__main__':
    print(addx(100))
    print(addx2(100))
