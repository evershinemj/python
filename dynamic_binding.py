#!/usr/bin/env python3
# encoding=utf-8

x = 5
addx = lambda y : x + y
x = 10
addx2 = lambda y : x + y

if __name__ == '__main__':
    print(addx(1))
    print(addx2(2))
    x = 100
    print(addx(1))
