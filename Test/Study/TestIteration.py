#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 17:16
# @Author  : iszhang
# @Email   : 
# @File    : TestIteration.py
# @software: PyCharm

# 注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
# 1. 有序集合：list，tuple，str和unicode；
# 2. 无序集合：set
# 3. 无序集合并且具有 key-value 对：dict

# 练习1：请用for循环迭代数列 1-100 并打印出7的倍数。
for x in range(1, 101):
    if x % 7 == 0:
        print x

# 练习2：zip()函数可以把两个 list 变成一个 list：
# >>> zip([10, 20, 30], ['A', 'B', 'C'])
# [(10, 'A'), (20, 'B'), (30, 'C')]
# 在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。

print zip([10, 20, 30], ['A', 'B', 'C'])
for x in zip([10, 20, 30], ['A', 'B', 'C']):
    print x[0], ' - ', x[1]
