import requests
from bs4 import BeautifulSoup
from getimg import header
from pyvar import url
import os
import os.path
##from getmovies import getsoup


def downjs(url, basename):
    """
    download javascript resources
    """
##    cnt = 1
    if(os.path.exists(basename) == 0):
        os.makedirs(basename)
        
    #reusable code block
    response = requests.get(url, headers = header)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    #reusable code block

    #calling a tag is like calling find_all
    #so soup('script') is equivalent to soup.find_all('script')
    scriptlist = soup.find_all('script')  #... = soup('script')
    for script in scriptlist:
##        note: the script tag doesn't neccesarily contain
##        the src attr!
##        must check before referrencing

        #important check step
        if 'src' in script.attrs:
            src = script['src']
            if(src.__contains__('http') == 0):
                pass
            else:
                print('downloading ' + src)
                suffix = src.split(r'/')[-1]
                res = requests.get(src, headers = header)
                js = res.text
                with open(basename + suffix, 'w') as f:
                    f.write(js)
        else:
            pass

basename = '/Users/wangxueming/imgjs/'

downjs(url, basename)
