#!/usr/bin/env python3
# encoding=utf-8


class Cafe:
    def __init__(self, name):
        self.name = name

    def desc(self, desc):
        self.desc = desc

    def __str__(self):
        return 'Cafe: {}'.format(self.name)


if __name__ == '__main__':
    satir = Cafe('Satir Coffee')
    print(satir)

