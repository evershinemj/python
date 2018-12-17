#!/usr/bin/env python3
# encoding=utf-8


def gen_chain(iterators):
    for i in iterators:
        yield from i


if __name__ == '__main__':
    ll = [['l1', 'l2', 'l3'], ('t1', 't2', 't3'), 'abc']
    for i in gen_chain(ll):
        print(i)

