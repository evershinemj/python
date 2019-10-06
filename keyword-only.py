#!/usr/bin/env python3
# encoding=utf-8


def showweather(*, weather):
    '''
    use an asterisk to indicate the end of positional args
    and the start of keyword args
    '''
    print('Today is {}'.format(weather))


if __name__ == '__main__':
    showweather(weather = 'sunny')
    try:
        showweather("windy")
    except Exception as e:
        print('Sorry, an exceptions occurred while '
                'calling showweather("windy")')
