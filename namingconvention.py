#!/usr/bin/env python3
# encoding=utf-8


class Customer:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __str__(self):
        pass
        return self.name

    def __repr__(self):
        pass
        return 'Customer: name=>{name} type=>{type} hobby=>{hobby}'.format(
                name = self.name, type = self.type_, hobby = self.__hobby)

    def __enter__(self):
        pass
        print('Hey, let\'s welcome Gene Kelly')
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        pass
        print('Bye, Gene Kelly')

    def _splitname(self):
        first = self.name.split()[0]
        last = self.name.split()[-1]
        # return a tuple
        return first, last

    def getfirstname(self):
        # first, _ = _splitname(self)[0]
        # should add self., as this is in 
        # function scope
        # first, _ = self._splitname(self)[0]
        # when calling a member function,
        # should not provide self as an arg;
        # adding self should only be done
        # in function defining
        # first, _ = self._splitname()[0]
        #
        # first = self._splitname()[0]
        # or 
        # first, _ = self._splitname()
        first, _ = self._splitname()
        return first

    def getlastname(self):
        # last = self._splitname()[-1]
        # or
        # _, last = self._splitname()
        _, last = self._splitname()
        return last

    def gethobby(self):
        return self.__hobby

    # appending an underscore to prevent clashing
    # with builtin function type()
    def type_(self):
        return self.type_

    # '__' indicates that the field will not be inherited
    # self.__hobby = 'singing', should not add self. in
    # class scope, as this is the default
    __hobby = 'singing'


if __name__ == '__main__':
    customer = Customer('Gene Kelly', 'humorous')
    with customer as c:
        print(c)
        print(repr(c))
        print('First name: ' + c.getfirstname())
        print('Last name: ' + c.getlastname())
        print('Type: ' + c.type_)
        print('Hobby: ' + c.gethobby())
