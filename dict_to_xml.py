#!/usr/bin/env python3
# encoding=utf-8
from xml.etree.ElementTree import Element, tostring
import json

with open('places.json', 'r') as f:
    places = json.load(f)
    e = Element('places')
    for key, val in places.items():
        child = Element(key)
        child.text = val
        e.append(child)
    print(tostring(e))    

