#!/usr/bin/env python3
# encoding=utf-8
import pickle

with open('serialization', 'rb') as f:
    sun = pickle.load(f)
    print('sun: ' + str(sun))
    print('sun.exists: ' + str(sun.exists))
    print('sun.desc: ' + sun.desc)
