#!/usr/bin/env python3
# encoding=utf-8
t1 = ('breakfast', 'lunch', 'supper')
t2 = ('bread', 'rice', 'noodles')
d = dict(zip(t1, t2))
for i in d:
    print(i)
for i in d.items():
    print(i)
