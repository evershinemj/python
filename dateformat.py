#!/usr/bin/env python3
# encoding=utf-8
from datetime import date

d = date(2018, 12, 18)

if __name__ == '__main__':
    print(format(d))
    print(format(d, '%A, %B %d, %Y'))
    print('Hey, today is {:%a, %b %d, %Y}'.format(d))
