#!/usr/bin/env python3
# encoding=utf-8
import copy

l = [1, 2, 3]  # not a compound object
a = [1, 3, 5]
b = [2, 4, 6]
c = [a, b]  # a compound object

if __name__ == '__main__':
    print('l: ' + str(l))
    print('lcopy = copy.copy(l)')
    lcopy = copy.copy(l)
    print('lcopy: ' + str(lcopy))
# is lcopy a new object?
    print('id(l) == id(lcopy)')
    print(id(l) == id(lcopy))
# are primitive type variables in lcopy new copies?
    print('id(l[0]) == id(lcopy[0])')
    print(id(l[0]) == id(lcopy[0]))

    d = copy.copy(c)
    # is d a new compound object?
    print('id(d) == id(c)')
    print(id(d) == id(c))
    # are objects in d new objects?
    print('id(d[0] == id(c[0]))')
    print(id(d[0]) == id(c[0]))


