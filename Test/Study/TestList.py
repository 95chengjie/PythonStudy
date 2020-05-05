#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 16:50
# @Author  : iszhang
# @Email   : 
# @File    : TestList.py
# @software: PyCharm

L = ['Adam', 'Lisa', 'Bart', 'Paul']
# 取出前3个元素；从索引0开始取，直到索引3为止
print L[:3], L[1:3]
# 每两个元素取出一个来，也就是隔一个取一个
print L[::2]

# range()函数可以创建一个数列：
# >>> range(1, 101)
# [1, 2, 3, ..., 100]
# 请利用切片，取出：
# 1. 前10个数；
# 2. 3的倍数；
# 3. 不大于50的5的倍数。
L = range(1, 101)
print L[:10], L[2::3], L[4:50:5]

# 利用倒序切片对 1 - 100 的数列取出：
# 1. 最后10个数；
# 2. 最后10个5的倍数。
print range(1, 101)[-10:], range(1, 101)[-46::5]

# 字符串有个方法 upper() 可以把字符变成大写字母：
# >>> 'abc'.upper()
# 'ABC'
# 但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
def firstCharUpper(x):
    return x[0].upper() + x[1:]
print firstCharUpper('name')
