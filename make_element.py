#!/usr/bin/env python3
# encoding=utf-8
import html


# def make_element(key, val, **attrs):
# **kwargs must be the last parameter
# it's impossible to add another keyword 
# parameter after **kwargs; that causes
# ambiguity


# refactored
def _attrs_parse(attrs:dict) -> str:
    '''
    function not as an interface,
    but for inner implementation only
    '''
    # adding a space as in ' %s="%s"' creates
    # standard and neat view
    # attrslist = [' %s="%s"' % i for i in attrs.items()]
    # refactored
    attrslist = [' %s="%s"' % i for i in attrs.items() if i[0] != 'class_']
    # refactored
    if 'class_' in attrs:
        attrslist.append(' class="' + attrs['class_'] + '"')
    attrs_str = ''.join(attrslist)
    return attrs_str
    

def make_element(key:str, val:str, **attrs):
    attrs_str = _attrs_parse(attrs)
    return '<{key}{attrs}>{val}</{key}>'.format(
            key = key,
            attrs = attrs_str,
            val = html.escape(val)
            )


def make_element_unescaped(key:str, val:str, **attrs):
    attrs_str = _attrs_parse(attrs)
    return '<{key}{attrs}>{val}</{key}>'.format(
            key = key,
            attrs = attrs_str,
            val = val
            )


def make_element_repeated(key:str, val:str, repeat:int, **attrs):
    attrs_str = _attrs_parse(attrs)
    return '<{key}{attrs}>{val}</{key}>\n\n'.format(
            key = key,
            attrs = attrs_str,
            val = val
            ) * int(repeat)  # must convert cmdline arg repeat from str to int


if __name__ == '__main__':
    input = make_element('input', 'Please enter your name: ', type = 'text',
            name = 'text', placeholder = 'name here')
    a = make_element('a', 'Click to <search>', href = 'http://www.google.com',
            target = '_blank')
    print(input)
    print(a)
