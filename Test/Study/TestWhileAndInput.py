#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 17:49
# @Author  : iszhang
# @Email   : 
# @File    : TestWhileAndInput.py
# @software: PyCharm

# 例1
# name = raw_input('Please enter your name: ')
# print 'Hello, ' + name

# 例2
# pets = ['cat', 'dog', 'pig', 'cat', 'cat', 'goldfish', 'rabbit']
# while 'cat' in pets:
#         pets.remove('cat')
#
# print pets

# 例3
sandwich_orders = ['tuna sandwich', 'piza sandwich']
finished_sandwichs = []
flag = True
while sandwich_orders:
    orders = sandwich_orders.pop()
    print 'I made your ' + orders
    finished_sandwichs.append(orders)
print 'The sandwichs is finished!'
for x in finished_sandwichs:
    print '\n' + x


