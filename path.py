from os.path import exists
import os.path

# path parsing depends on the current working directory
dir(os.path)
ifexists = exists('text.txt')
user = os.path.expanduser('~')
var = os.path.expandvars('$SHELL')
file = '/Users/wangxueming/text.txt'
dirname = os.path.dirname(file)
expanded_dirname = os.path.dirname(os.path.expanduser('~/text.txt'))
basename = os.path.basename(file)
abspath = os.path.abspath('text.txt')
size = os.path.getsize('text.txt')
isdir = os.path.isdir('text.txt')
isfile = os.path.isfile('text.txt')
islink = os.path.islink('text.txt')


