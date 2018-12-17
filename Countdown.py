#!/usr/bin/env python3
# encoding=utf-8

class Countdown:
    def __init__(self, start):
        self._start = start

    def __iter__(self):
        n = self._start
        while n > 0:
            yield n
            n -= 1

    # def reverse_iter(self):
    def __reversed__(self):
        n = 1
        while n <= self._start:
            yield n
            n += 1


if __name__ == '__main__':
    countdown = Countdown(10)
    print('calling __iter__')
    for i in countdown:
        print(i)
    # print('calling reverse_iter')
    print('calling reversed')
    # for i in countdown.reverse_iter():
    for i in reversed(countdown):
        print(i)
        
