# must put digit after >, < or ^
raquo = '{:>5}'.format('abc')
laquo = '{:<5}'.format('abc')
caret = '{:^5}'.format('abc')

s = '{0!s:>10}'.format(1)
r = '{1!r:>10}|{0!r:^10}'.format('hey', 'funny')

comma = '{:,}'.format(1234)
pencent = '{:%}'.format(0.1)

print(repr(raquo))
print(repr(laquo))
print(repr(caret))
print(s)
print(r)
print(comma)
print(pencent)
