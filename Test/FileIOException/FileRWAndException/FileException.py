#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 17:15
# @Author  : iszhang
# @Email   : 
# @File    : FileException.py
# @software: PyCharm

filename = 'Book'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print 'the file ' + filename + ' is noe exist'
else:
    print len(contents)
