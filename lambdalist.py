#!/usr/bin/env python3
# encoding=utf-8

funcs = [lambda x, n=n : x + n for n in range(10)]

if __name__ == '__main__':
    print('calling f(100) in each iteration')
    for idx, f in enumerate(funcs):
        print('f: lambda x, n={} : x + n'.format(idx))
        print(f(100))
