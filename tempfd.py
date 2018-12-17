#!/usr/bin/env python3
# encoding=utf-8
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory

with TemporaryFile('w+t') as f:
    f.write('heyheyhey')
    f.seek(0)
    data = f.read()
    print(data)

with NamedTemporaryFile('w+t') as f:
    f.write('I\'m NamedTemporaryFile')
    f.seek(0)
    data = f.read()
    print(data)
    print(f.name)

with TemporaryDirectory() as d:
    print('dirname: ' + d)
