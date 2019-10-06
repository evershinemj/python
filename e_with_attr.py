#!/usr/bin/env python3
# encoding=utf-8
from xml.etree.ElementTree import Element, tostring
import json

e = Element('places')
e.set('for', 'study')
with open('places.json', 'r') as f:
    places = json.load(f)
    for k, v in places.items():
        child = Element(k)
        if k == 'cafeteria':
            child.set('desc', 'warm')
        elif k == 'KFC':
            child.set('desc', 'casual')
        child.text = str(v)
        e.append(child)
    print(tostring(e))

