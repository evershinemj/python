#!/usr/bin/env python3
# encoding=utf-8


_formats = {
        'ymd' : '{d.year}-{d.month}-{d.day}',
        'mdy' : '{d.month}/{d.day}/{d.year}',
        }


class Date:
    def __init__(self, year, day, month):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return 'year: {0.year}, month: {0.month}, day: {0.day}'.format(self)

    def __repr__(self):
        return '<Date> year: {0.year!r}, month: {0.month!r}, day: {0.day!r}'.format(self)

    def __format__(self, code):
        return _formats[code].format(d = self)


if __name__ == '__main__':
    date = Date(2018, 12, 18)
    print(format(date, 'ymd'))
    print('{:mdy}'.format(date))
