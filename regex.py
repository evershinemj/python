#!/usr/bin/env python3
import re

re.search('p', 'python')
re.search('y', 'python')
re.search('py', 'python')
re.search('th', 'python')
re.search('^py','python')
re.search('^py','python')
re.search('^p.*$','python')
re.search('^p.*$','python')
re.search('^[op].','python')
re.search('(o|p).+[mn]','python')

print(re.search('p', 'python'))
re.match('th','python')
re.match('[op]y','python')

re.findall('[a-z]', 'python')
re.findall('[py]', 'python')
re.findall('^p|n$', 'python')

text = "I'm happily and attentively editing the text."
re.findall(r'\w+ly', text)

pattern = re.compile(r'[abc]\w+?[rst]')
string = "I'm about to have some fun. Absolutely!"
re.sub(pattern, 'funny', string)
