#!/usr/bin/env python3
# encoding=utf-8
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @area.setter
    def area(self, val):
        if not isinstance(val, int) or not isinstance(val, float):
            raise TypeError('Expected int or float!')

    @area.deleter
    def area(self):
        raise AttributeError('Cannot delete attribute area!')

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @perimeter.setter
    def perimeter(self, val):
        if not isinstance(val, int) or not isinstance(val, float):
            raise TypeError('Expected int or float!')

    @perimeter.deleter
    def perimeter(self):
        raise AttributeError('Cannot delete attribute area!')


if __name__ == '__main__':
    circle = Circle(3)
    print('area: %s' % circle.area)
    print('perimeter: %s' % circle.perimeter)
    # dir(TypeError)
    try:
        circle.area = 'hey'
    except TypeError as te:
        print('Look, TypeError!')
        print(te)
    finally:
        print('Caught an exception!')

    try:
        del circle.area
    except AttributeError as ae:
        print('Look, AttributeError!')
        print(ae)
    finally:
        print('Caught an exception!')

    try:
        circle.perimeter = 'funny'
    except TypeError as te:
        print('Look, TypeError!')
        print(te)
    finally:
        print('Caught an exception!')

    try:
        del circle.perimeter
    except AttributeError as ae:
        print('Look, AttributeError!')
        print(ae)
    finally:
        print('Caught an exception!')
