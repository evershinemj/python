import random

l = []
for i in range(1, 30, 2):
    l.append(i)
for i in range(1, 16):
    # !s stands for conversion to str
    if i == 1:
        calltime = 'call random.choice for  1st time: '
    elif i == 2:
        calltime = 'call random.choice for  2nd time: '
    else:
        calltime = 'call random.choice for {0!s:>2}th time: '.format(i)
    print('{0}{1!s}'.format(calltime, random.choice(l)))
