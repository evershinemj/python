import random

l = [i for i in range(30) if i % 3 == 0]
print(l)
# note: random.shuffle() returns None
# print the list directly to see the result
# print(random.shuffle(l))
for i in range(1, 16):
    # !s stands for conversion to str
    if i == 1:
        calltime = 'call random.shuffle for  1st time: '
    elif i == 2:
        calltime = 'call random.shuffle for  2nd time: '
    else:
        calltime = 'call random.shuffle for {0!s:>2}th time: '.format(i)
#     print('{0}{1!s}'.format(calltime, random.shuffle(l)))
    random.shuffle(l)
    print(calltime + str(l))
