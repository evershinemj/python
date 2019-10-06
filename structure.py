#!/usr/bin/env python3
# encoding=utf-8
class Structure:
    def __init__(self, *args):
        if len(self._fields) != len(args):
            raise TypeError('expected {} arguments'.format(len(self._fields)))
        for name, val in zip(self._fields, args):
            # name = val
            setattr(self, name, val)


class Point(Structure):
    pass
    _fields = ['x', 'y']
    def __str__(self):
        return 'x: {} , y: {}'.format(self._fields[0], self._fields[-1])


class Circle(Structure):
    pass
    _fields = ['r']
    def __str__(self):
        return 'r: {}'.format(self._fields[0])


if __name__ == '__main__':
    p = Point(1, 2)
    c = Circle(3)
    print(p)
    print(c)
    p = Point(1, 2, 3)
    c = Circle(3, 4)
    
