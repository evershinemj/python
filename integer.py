#!/usr/bin/env python3
# encoding=utf-8
class Integer:
    '''
    note the use of magic methods
    __get__, __set__ and __delete__
    '''
    def __init__(self, name):
        self.name = name
        pass

    # cls for class (avoid conflicting with the keyword class)
    def __get__(self, instance, cls):
        '''
        automatically called when access an attribute
        with the dot operator 
        '''
        return instance.__dict__[self.name]

    def __set__(self, instance, val):
        '''
        automatically called in assignment
        '''
        if not isinstance(val, int):
            raise TypeError('Expected an argument of type int!')
        instance.__dict__[self.name] = val
        print('set value to: ' + str(val))
        pass

    def __delete__(self, instance):
        '''
        automatically called when using the 
        del statement
        '''
        if instance.__dict__[self.name] is None:
            raise AttributeError('No such attribute!')
        print('deleted ' + self.name)
        pass


class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(1, 2)
    print(p.x)
    p.y = 3
    print(p.y)
    del p.x
    p.x = '4'
    
