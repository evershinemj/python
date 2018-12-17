#!/usr/bin/env python3
# encoding=utf-8
import pickle

class Sun:
    '''
    exists: of type bool
    '''
    def __init__(self, exists):
        self.exists = exists

    '''
    return a description as to 
    whether the sun is warm or cold
    '''
    def desc(self):
        return self.desc

sun = Sun(True)
sun.desc = 'warm'
f = open('serialization', 'wb')
pickle.dump(sun, f)
