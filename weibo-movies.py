#!/usr/bin/env python3
# encoding=utf-8

import requests
from bs4 import BeautifulSoup
# from getsoup import getsoup
import os
import os.path
from urllib.request import urlopen
import getresp
from getsoup import getsoup


# headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11', 'Referer': 'https://weibo.com/'} 
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11', 'Referer': 'https://www.weibo.com/'} 


# def getsoup(html) -> BeautifulSoup:
#     soup = BeautifulSoup(html, 'lxml')
#     return soup


# def getresp(url):
#     global headers
#     # print(headers)
#     # r = requests.get(url, headers = headers)
#     r = urlopen(url)
#     # print('r.headers: ')
#     # print(r.headers)
#     # print('url: ')
#     # print(url)
#     return r


if __name__ == '__main__':
    # not in a function, should not declare global here
    # global headers
    #
    # url = 'https://weibo.com/?category=10018'
    url = 'https://www.weibo.com/?category=10018'
    url = 'https://weibo.com/ttarticle/p/show?id=2309404329744106698548'
    url = 'https://weibo.com/2447680824/Hcvz3rSIQ?ref=feedsdk&type=comment#_rnd1547816593132'

    # url = 'https://www.zhihu.com/question/49441554/answer/540280872'
    # url = 'https://www.zhihu.com/question/49441554/'
    # url = 'https://www.zhihu.com/question/38485891/answer/235956626'
    # html = gethtml(url)
    #
    # r = getresp(url)
    #
    # r = getresp.getresp(url)
    #
    # print('r.url: ')
    # print(r.url)
    # r = getresp(url, headers = headers)
    # html = r.text
    #
    # html = r.read()
    #
    # html = getresp.get_resp_content(url)
    response = getresp.getresp(url, headers)
    print(headers)
    print(response.status_code)
    # print(response)


    # print(r)
    # print(dir(r))
    # print('r.url: ')
    # print(r.url)
    # print('r.code: ')
    # print(r.code)
    # print('r.getheaders()')
    # print(r.getheaders())

    # print(html)
    # print('length of html in terms of chars: ')
    # print(len(html))
    html = response.text

    # response = urlopen(url)
    # html = response.read()
    print(html)
    soup = getsoup(html)
    imgs = soup.find_all('img')
    # print(imgs)
    imgcnt = 0
    # for img in imgs:
    # for img in soup.find_iter('img'):
    # for img in soup.finditer('img'):
    
    # while (img = soup .find('img')) is not None:
    for img in soup.find_all('img'):
        print(img)
        print()
        src = img['src']
        print('\033[7msrc: \033[0m' + src)
        # if not os.path.exists('zhihu-icons')
        # if not os.path.exists('zhihu-icons'):
        #     os.mkdir('zhihu-icons')
        if not os.path.exists('weibo-movie-images'):
            os.mkdir('weibo-movie-images')
        # with open('zhihu-icons/img' + str(imgcnt)) as f:
        # bug found:
        # default open mode: 'r'
        # must specify 'w'
        #
        # with open('zhihu-icons/img' + str(imgcnt), 'w') as f:
        with open('weibo-movie-images/img' + str(imgcnt) + '.jpg', 'wb') as f:
            # to be refactored:
            # some images are empty
            if src.startswith('http'):
                # f.write(getresp(src).content)
                # f.write(getresp(src))
                # f.write(getresp(src).read())
                f.write(getresp.get_resp_content(src))
        imgcnt += 1
