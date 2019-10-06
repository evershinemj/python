#!/usr/bin/env python3
# encoding=utf-8
import copy
from copytest import l, a, b, c

ldcopy = copy.deepcopy(l)
print('ldcopy = copy.deepcopy(l)')
print(ldcopy)
# is ldcopy a new object?
print('id(ldcopy) == id(l)')
print(id(ldcopy) == id(l))
# are primitive type variables in lcopy new copies?
print('id(ldcopy[0]) == id(l[0])')
print(id(ldcopy[0]) == id(l[0]))

d = copy.deepcopy(c)
# is d a new compound object?
print('id(d) == id(c)')
print(id(d) == id(c))
# are objects in d new objects?
print('id(d[0] == id(c[0]))')
print(id(d[0]) == id(c[0]))
