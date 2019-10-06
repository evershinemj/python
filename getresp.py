from urllib.request import urlopen
# bug found:
# HTTPResponse not defined
# import http.client.HTTPResponse
from http.client import HTTPResponse

import requests

headers = {'User-Agent' : 'Mozilla/5.0', 'Referer': 'https://www.baidu.com'} 
# headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11', 'Referer': 'https://www.weibo.com'} 


# def getresp(url) -> HTTPResponse:
def getresp(url, headers) -> HTTPResponse:
    '''
    returns http.client.HTTPResponse
    '''
    r = requests.get(url, headers=headers)
    return r


def get_resp_content(url):
    r = urlopen(url)
    content = r.read()
    return content
