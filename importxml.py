#!/usr/bin/env python3
# encoding=utf-8
from urllib.request import urlopen
# import xml.etree
from xml.etree.ElementTree import parse

u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    pubDate = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(pubDate)
    print(link)
    print()
