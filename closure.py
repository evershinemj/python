#!/usr/bin/env python3
# encoding=utf-8
import callback


def make_handler():
    cnt = 0
    def handle(res):
        nonlocal cnt
        cnt += 1
        print('<{}>: {}'.format(
            cnt, res))
    # handle(res)
    # refactored: magic happens when you RETURN 
    # the inner function
    return handle


if __name__ == '__main__':
    ##############################################################
    # for x, y in zip(range(1, 11), range(2, 22, 2)):            #
    #     h = make_handler()                                     #
    #     callback.apply_async(callback.add, (x, y), callback=h) #
    ##############################################################

    # IMPORTANT: for closure to work as expected, should call
    # outer function only once, and inner function multiple 
    # times
    h = make_handler()
    for x, y in zip(range(1, 11), range(2, 22, 2)):
        callback.apply_async(callback.add, (x, y), callback=h)
