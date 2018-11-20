#!/usr/bin/env python
# encoding=utf-8

import requests
import re
import os
import os.path
from bs4 import BeautifulSoup
from pyvar import url
from getimg import header

def getcss(url, basename):
    if(os.path.exists(basename) == 0):
        os.makedirs(basename)
    response = requests.get(url, headers = header)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

# csslist = soup("link", rel = "stylesheet")
    csslist = soup("link", type = "text/css")
    for css in csslist:
        href = css['href']
        print('downloading ' + href)
        filename = href.split(r'/')[-1]
        res = requests.get(href, headers = header)
        page = res.text
        with open(basename + '/' + filename, 'w') as f:
            f.write(page)


basename = '/Users/wangxueming/imgcss/'
getcss(url, basename)
