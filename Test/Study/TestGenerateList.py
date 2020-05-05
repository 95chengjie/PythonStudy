#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 17:40
# @Author  : iszhang
# @Email   : 
# @File    : TestGenerateList.py
# @software: PyCharm

# 练习1：生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x * x)
print L
# 列表生成式
print [x * x for x in range(1, 11)]

# 练习2：请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print [x * (x + 1) for x in range(1, 100, 2)]

# 练习3：请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]
print toUppers(['Hello', 'world', 101])

# 练习4：利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
# 使用列表生成式
print [100 * x + 10 * y + z for x in range(1, 10) for y in range(10) for z in range(10) if x == z]