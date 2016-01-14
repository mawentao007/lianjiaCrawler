#coding:utf-8
__author__ = 'marvin'

import re
a = ['a','\r\n','\r\n     ']
a = [x.strip() for x in a]
a = filter(None,a)
print a

w = ""