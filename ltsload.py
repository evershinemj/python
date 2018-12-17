'''
load list, tuple and set
from a file
'''
import pickle

with open('pickledump', 'rb') as f:
    print('l = pickle.load(f)')
    l = pickle.load(f)
    print(l)
    print('t = pickle.load(f)')
    t = pickle.load(f)
    print(t)
    print('s = pickle.load(f)')
    s = pickle.load(f)
    print(s)
