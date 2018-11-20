import requests
from bs4 import BeautifulSoup

__doc__ = \
"""
this module provides easy access to
getting images from a certain url
"""

start = 200
offset = 10
path = '/Users/wangxueming/atlases'
header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'} 

def getimg(url, start, offset, path):
    """
    this is function getimg
    in module getimg
    """

    for i in range(offset):
        pageurl = url + str(start + i)
        atlasname = 'atlas' + str(start + i) 
        r = requests.get(pageurl, headers = header)
        page = r.text
        soup = BeautifulSoup(page, 'lxml')
        imglist = soup.find_all('img')
        imgcnt = 1
    
        for img in imglist:
            src = img['src']
            res = requests.get(src, headers = header)
            with open(path + '/' + atlasname + '.img' + str(imgcnt) + '.jpg' ,'wb') as f:
                f.write(res.content)
            imgcnt += 1

