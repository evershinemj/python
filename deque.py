from collections import deque
d = deque(maxlen = 5)
for i in range(1, 6):
    d.append(i)
    print('appended ' + str(i) + ' to deque d')
print()
print('d now becomes ' + str(d))
print('d.append(6)')
d.append(6)
print('d now becomes ' + str(d))
print('d.appendleft(7)')
d.appendleft(7)
print('d now becomes ' + str(d))
print('d.pop()')
d.pop()
print('d now becomes ' + str(d))
print('d.popleft()')
d.popleft()
print('d now becomes ' + str(d))