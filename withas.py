#!/usr/bin/env python3
# encoding=utf-8


class Coffee:
    def __init__(self, name):
        self.name = name
        pass

    def __str__(self):
        pass
        return self.name

    def __repr__(self):
        pass

    def __format__(self):
        pass

    def __enter__(self):
        print('Entering cafe...')
        # IMPORTANT
        # need to return self
        # to store in the varible
        # specified after as
        return self

    # def __exit__(self):
    # __exit__ needs three args apart from self:
    # exception type, exception value, and traceback
    def __exit__(self, exc_tp, exc_val, traceback):
        print('Leaving cafe...')


if __name__ == '__main__':
    coffee = Coffee('American coffee') 
    with coffee as c:
        print('Drinking ' + str(c))
        # print(c.name)
        # print(c)
        # pass
        #
        # four args are passed into __exit__ here
