#!/usr/bin/env python3
# encoding=utf-8


def apply_async(add, t, *, callback):
    r = add(*t)
    callback(r)


def add(a, b):
    return a + b


def print_result(r):
    print('The result of calling add is: %s' % r)


if __name__ == '__main__':
    apply_async(add, (1, 2), callback=print_result)
