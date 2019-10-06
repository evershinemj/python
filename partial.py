#!/usr/bin/env python3
# encoding=utf-8
from functools import partial
from make_element import make_element

p = partial(make_element, 'div')
print(p('inside the div', width = '100px', height = '100px'))

p = partial(make_element, 'span', 'inside the span')
print(p(style = 'font-size: 30px; font-weight: bold'))

p = partial(make_element, color = 'blue')
print(p('em', 'happy'))
