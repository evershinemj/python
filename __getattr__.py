#!/usr/bin/env python3
# encoding=utf-8


class Idoit:
    def __init__(self):
        pass

    def do(self):
        print('Let me do it')


class Delegate:
    # _idoit = Idoit()

    def __init__(self):
        pass
        self._idoit = Idoit()

    def __getattr__(self, name):
        return getattr(self._idoit, name)


if __name__ == '__main__':
    d = Delegate()
    d.do()
