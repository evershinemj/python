#!/usr/bin/env python3
# encoding=utf-8


namelist = ['Michael Jackson', 'Jay Chou', 'Jackie Chan', 'Albert Einstein']
sortedlist = sorted(namelist, key = lambda x : x.split()[-1].lower())


if __name__ == '__main__':
    print('original list: {0}'.format(namelist))
    print('calling sorted(namelist, key = lambda x : x.split()[-1].lower())')
    print('sortedlist: {0}'.format(sortedlist))
