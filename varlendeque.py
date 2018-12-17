from collections import deque
d = deque()
for i in range(10):
    d.appendleft(i)
print(d)
print('d.append(11)')
d.append(11)
print('d now is: ' + str(d))
print('d.popleft()')
d.popleft()
print('d now is: ' + str(d))
