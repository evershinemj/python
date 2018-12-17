#!/usr/bin/env python3
# encoding=utf-8
import os

for dirpath, dirnames, filenames in os.walk('.'):
    print(dirpath, dirnames, filenames)
