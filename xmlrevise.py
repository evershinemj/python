#!/usr/bin/env python3
# encoding=utf-8
#
# ElementTree is a module
# xml/etree/ElementTree.py
from xml.etree.ElementTree import parse, tostring, Element

doc = parse('torevise.xml')
root = doc.getroot()
e = Element('breakfast')
e.text = 'none'
d = doc.find('dinner')
n = Element('nightmeal')
n.text = 'none'
print(tostring(root))
for child in root.getchildren():
    print(tostring(child))
print()
print('root.insert(0, e)')
root.insert(0, e)
print('root.append(n)')
root.append(n)
print(tostring(root))
for child in root.getchildren():
    print(tostring(child))
print()
print('root.remove(root.find("lunch"))')
root.remove(root.find("lunch"))
print(tostring(root))
for child in root.getchildren():
    print(tostring(child))
print()
# with open('addelement.xml', 'w') as f:
#     doc.write(f)
doc.write('addelement.xml', xml_declaration = True)
