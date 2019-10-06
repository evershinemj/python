import random

for i in range(10):
    randi = random.randint(0, 10) # including 0 and 10
    if i == 0:
        print('calling random.randint(0, 10)  1st time gets: ', end = '')
    elif i == 1:
        print('calling random.randint(0, 10)  2nd time gets: ', end = '')
    else:
        # help(str.format)
        # help(format)
        # help('FORMATTING')
        calltime = 'calling random.randint(0, 10) {:>2}th time gets: '.format(
                str(i + 1))  # > for right aligning
        print(calltime, end = '')
    print(randi)

