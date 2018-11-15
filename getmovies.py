#!/bin/bash
# encoding=utf-8

import requests
import re
from bs4 import BeautifulSoup
from getimg import header

if __name__ == '__main__':
    print('executing ' + __name__)

url = 'https://www.dytt8.net'


def getsoup(url) -> BeautifulSoup:
    """ 
    a tiny function defined in order to be called
    by other functions which require a argument of
    type BeautifulSoup
    """
    response = requests.get(url, headers = header)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    return soup


def dumphtml(url): 
    """
    dump html to stdout
    """
    soup = getsoup(url)
    print(soup.prettify())


def getmovielist(url):
    """
    get a movie list as defined by <ul> tag
    """
    soup = getsoup(url)
    a_list = soup.find('ul').find_next('ul').find_all('a')
    for item in a_list:
        print(item.string)


getmovielist(url)
