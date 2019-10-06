#!/usr/bin/env python3
# encoding=utf-8
import callback


class ResultHandler:
    def __init__(self):
        self.cnt = 0

    def handle(self, result):
        self.cnt += 1
        if self.cnt % 10 == 1:
            suffix = 'st'
        elif self.cnt % 10 == 2:
            suffix = 'nd'
        elif self.cnt % 10 == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
        print('{}{} result: {}'.format(
            self.cnt, suffix, result))


if __name__ == '__main__':
    rh = ResultHandler()
    callback.apply_async(callback.add, (100, 200), callback = rh.handle)
    callback.apply_async(callback.add, (200, 300), callback = rh.handle)
    callback.apply_async(callback.add, (300, 400), callback = rh.handle)
    callback.apply_async(callback.add, (400, 500), callback = rh.handle)
