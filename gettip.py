import random
import sys
import math
import time


def getlinelist():
    '''
    generate a list of lines from a given file
    '''

    # use !!ls ~/*凡遇*图释* to filter the current
    # line through shell command

    # add 'autocmd FileType *   set formatoptions+=r' to .vimrc
    
    linelist = []
    # textwidth set to 80 by ftplugin in .vim
    # hence can perform gq in visual mode to format the following lines

    # note: in original file '凡遇要处总诀.txt', there were Chinese periods at
    # the end of every line. Thus the search pattern should be /。 *$/, where
    # the blank in the pattern is a Chinese period
    file = '/Users/wangxueming/凡遇要处总诀.txt'
    with open(file, 'r') as f:
        # while (line = f.readline()) != None:
            # linelist.append(line)
        linelist = f.readlines()
    return linelist


linelist = getlinelist()
linenum = len(linelist)


def printtip():
    global linelist
    global linenum
    rand = random.randint(0, math.floor(linenum / 2 - 1)) * 2
    # print(linelist[rand].strip())
    # print(linelist[rand + 1].strip())
    strlist1 = list(linelist[rand].strip())
    strlist2 = list(linelist[rand + 1].strip())
    for char in strlist1:
        print(char, end = '')
        # print(char)
        # time.sleep(0.1)
    time.sleep(1)
    print()
    for char in strlist2:
        print(char, end = '')
        # print(char)
    time.sleep(1)
    print()


printtip()
