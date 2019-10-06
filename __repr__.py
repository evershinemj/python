#!/usr/bin/env python3
# encoding=utf-8


class Lunch:
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price

    def setprice(self, price):
        self.price = price

    def getprice(self) -> int:
        return self.price

    def setname(self, name):
        self.name = name

    def getname(self) -> str:
        return self.name

    def __repr__(self):
        return 'Lunch: name=>{0.name!r} price=>{0.price!r}'.format(
                self)


if __name__ == '__main__':
    lunch = Lunch('chicken', 17)
    print(lunch.__repr__())
