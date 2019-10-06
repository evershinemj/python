#!/usr/bin/env python3
# encoding=utf-8
import html


# use :<type> notation to annotate arg types
def make_element(key:str, val:str, **attrs) -> str:
    attrslist = [' %s="%s"' % i for i in attrs.items()]
    attrs_str = ''.join(attrslist)
    return '<{key}{attrs}>{val}</{key}>'.format(
            key = key,
            val = html.escape(val),
            attrs = attrs_str
            )


if __name__ == '__main__':
    h1 = make_element('h1', '"Sunny Today!"', style = 'color:cyan')
    print(h1)
    print(make_element.__annotations__)
