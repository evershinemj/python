#!/usr/bin/env python3
# encoding=utf-8
# from collections import Iterable
# this form of import doesn't raise warning
from collections.abc import Iterable  


class Songlist(Iterable):
    '''
    the advantage of inheriting collections.Iterable
    is that is you do not implement __init__, an
    exception will be raised
    '''
    def __init__(self, *args):
        self.songs = args

    def __iter__(self):
        return iter(self.songs)


if __name__ == '__main__':
    songlist = Songlist('半岛铁盒', '轨迹', '东风破', '发如雪')
    for s in songlist:
        print(s)
