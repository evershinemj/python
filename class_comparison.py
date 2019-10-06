#!/usr/bin/env python3
# encoding=utf-8
from functools import total_ordering


@total_ordering
class Table:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width

    def __str__(self):
        return 'Table of length {} and width {}'.format(
                self.length, self.width)

    def __eq__(self, other):
        '''
        magic method called when using 
        the == operator
        '''
        return self.area == other.area
        
    def __lt__(self, other):
        '''
        magic method called when using 
        the < operator
        '''
        return self.area < other.area

    ####################################################################################################
    #  / ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \  #
    # |  /~~\                                                                                  /~~\  | #
    # |\ \   |  __gt__ = lambda self, other : not (self.__eq__(other) or self.__lt__(other))  |   / /| #
    # | \   /|  __le__ = lambda self, other : self.__eq__(other) or self.__lt__(other)        |\   / | #
    # |  ~~  |  __ge__ = lambda self, other : not self.__lt__(other)                          |  ~~  | #
    # |      |  __ne__ = lambda self, other : not self.__eq__(other)                          |      | #
    # |      |                                                                                |      | #
    # |      |  __gt__ = lambda self, other : not (self == other or self < other)             |      | #
    # |      |  __le__ = lambda self, other : self == other or self < other                   |      | #
    # |      |  __ge__ = lambda self, other : not (self < other)                              |      | #
    # |      |  __ne__ = lambda self, other : not (self == other)                             |      | #
    # |      |                                                                                |      | #
    #  \     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|     /  #
    #   \   /                                                                                  \   /   #
    #    ~~~                                                                                    ~~~    #
    ####################################################################################################

if __name__ == '__main__':
    t1 = Table(10, 10)
    t2 = Table(5, 15)
    t3 = Table(9, 9)
    print('t1 < t2: ' + str(t1 < t2))
    print('t3 > t2: ' + str(t3 > t2))
    print(max(t1, t2, t3))
    print(min(t1, t2, t3))
