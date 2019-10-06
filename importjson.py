#!/usr/bin/env python3
# encoding=utf-8
import json

places = {
        'cafeteria' : 'quiet',
        'KFC' : 'provides food'
        }
with open('places.json', 'w') as f:
    json.dump(places, f)
with open('places.json', 'r') as f:
    places = json.load(f)
    print(type(places))
    print(places)
    for i, j in places.items():
        print('key: ' + i + ' => ' +'val: ' + j)
