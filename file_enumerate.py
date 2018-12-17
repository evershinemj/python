#!/usr/bin/env python3
# encoding=utf-8
with open('iter.py', 'r') as f:
    for lineno, line in enumerate(f, 1):  # start index is 1
        # append end = '' when enumerating a file
        # as linebreak is contained in each item being enumerated
        print(lineno, line, end = '')  
