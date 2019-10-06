#!/usr/bin/env python3
# encoding=utf-8


def avg(first, *rest):
    total = first + sum(rest)
    num = 1 + len(rest)
    return float(total / num)


if __name__ == '__main__':
    avg1 = avg(1, 2, 3, 4)
    print('average of 1, 2, 3 and 4: %f' % avg1)
    avg2 = avg(2, 3, 5, 7)
    print('average of 2, 3, 5 and 7: %f' % avg2)
    avg3 = avg(1, 4, 9, 16)
    avg4 = avg(2, 4, 6, 8)
    print('avg(1, 4, 9, 16): %f\tavg(2, 4, 6, 8): %f' % (avg3, avg4))

