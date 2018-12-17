#!/usr/bin/env python3
# encoding=utf-8
import pickle

with open('pickledump', 'wb') as f:
    pickle.dump([1, 2, 3, 4], f)
    pickle.dump((1, 3, 5, 7), f)
    pickle.dump(set((1, 4, 9, 16,)), f)
