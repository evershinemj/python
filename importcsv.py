#!/usr/bin/env python3
# encoding=utf-8
import csv

with open('dinner.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    for row in f_csv:
        print(row)
