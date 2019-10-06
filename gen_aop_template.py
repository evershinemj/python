#!/usr/bin/env python3
# encoding=utf-8
import make_element
import sys
from functools import partial

  #################################################################
  #  _____________________________________________________        #
  # /                                                     \       #
  # |  use sys.argv to access command line arguments      |       #
  # \_______________________________________________  __'\        #
  #                                                 |/   \\       #
  #                                                  \    \\  .   #
  #                                                       |\\/|   #
  #                                                       / " '\  #
  #                                                       . .   . #
  #                                                      /    ) | #
  #                                                     '  _.'  | #
  #                                                     '-'/    \ #
  #                                                               #
  #################################################################

  # command line arguments include the module itself 
  # as the first argument
  
arglist = sys.argv
filename = arglist[1]
repeat = arglist[2]
# pep8 standard: no whitespace around
# keyword parameter and argument assignment
print('writing to {f}...'.format(f=filename))

print('type of make_element: {}'.format(type(make_element)))
print(('type of make_element.make_element: '
        '{}').format(type(make_element.make_element)))
with open(filename, 'w') as f:
    f.write('''\
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.springframework.org/schema/beans 
      http://www.springframework.org/schema/beans/spring-beans.xsd">

'''
    )
    ################################################################
    #  ________________________________________________________    #
    # /\                                                       \   #
    # \_| # bug detected                                       |   #
    #   | # subtle error: make_element is the module name here |   #
    #   | # should use make_element.make_element instead       |   #
    #   |   ___________________________________________________|_  #
    #    \_/_____________________________________________________/ #
    ################################################################

    # p = partial(make_element, 'bean', 'constructor-arg ref="" /')
    p = partial(make_element.make_element_repeated, 'bean',
        '\n  <constructor-arg ref="" />\n', repeat)
    # bean = p(id = '', class = '')
    # cannot use class as keyword parameter
    # use class_ instead
    bean = p(id = '', class_ = '')
    aop = make_element.make_element_unescaped('aop:config',
'''
    <aop:aspect ref="">
      <aop:pointcut id=""
          expression="execution()"/>
        
      <aop:before pointcut-ref="" 
          method=""/>

      <aop:after pointcut-ref="" 
          method=""/>
    </aop:aspect>
''')  
    # NOTE: no indent before ''', thus </aop:config>
    # will be properly formatted (no indent)


    f.write(bean)
    # f.write('\n' * 2)
    f.write(aop)
    f.write('\n' * 2)
    f.write('</beans>')
