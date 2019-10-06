from bs4 import BeautifulSoup


def getsoup(html) -> BeautifulSoup:
    '''
    returns a BeautifulSoup instance 
    from a given html
    '''
    soup = BeautifulSoup(html, 'lxml')
    return soup
