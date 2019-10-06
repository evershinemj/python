#!/usr/bin/env python3
# encoding=utf-8
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('Drawing a circle...')


class Rectangle(Shape):
    def draw(self):
        print('Drawing a rectangle...')


if __name__ == '__main__':
    c = Circle()
    c.draw()
    r = Rectangle()
    r.draw()
