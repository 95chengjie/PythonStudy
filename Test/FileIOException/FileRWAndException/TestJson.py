#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 18:02
# @Author  : iszhang
# @Email   : 
# @File    : TestJson.py
# @software: PyCharm

import json

numbers = [2, 3, 4, 5, 6, 7]
filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

filename = 'numbers.json'
with open(filename) as file_object:
    json.load(file_object)