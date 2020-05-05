#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 15:11
# @Author  : iszhang
# @Email   : 
# @File    : TestFunction.py
# @software: PyCharm

import math

# 练习1：sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
x = 1
L = []
while x <= 100:
    L.append(x * x)
    x += 1

print sum(L)

# 练习2：自定义求绝对值
def abs1(x):
    if x >= 0:
        return x
    else:
        return -x

print abs1(-1)

# 练习3：请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和
def square_of_sum(L):
    sum = 0
    for x in L:
        sum = sum + x * x
    return sum

print square_of_sum([1, 2, 3])

# 练习4：一元二次方程的定义是：ax² + bx + c = 0
# 请编写一个函数，返回一元二次方程的两个解。
# 注意：Python的math包提供了sqrt()函数用于计算平方根。
def quadratic_equation(a, b, c):
    d = b * b - 4 * a * c
    a1 = 0
    a2 = 0
    d2 = 0
    if d >= 0:
        d2 = math.sqrt(d)
        a1 = (-b + d2) / (2 * a)
        a2 = (-b - d2) / (2 * a)
        return a1, a2
    else:
        return '该二元一次方程无解'
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
print quadratic_equation(1, 2, 3)

# 练习5：计算阶乘 n! = 1 * 2 * 3 * ... * n，用函数 fact(n)表示
def fact(n):
    if n == 1:
        return 1
    return n * fact(n -1)
print fact(5)
print fact(1)

# 练习6：汉诺塔 (http://baike.baidu.com/view/191666.htm) 的移动也可以看做是递归函数。
# 我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
# 如果a只有一个圆盘，可以直接移动到c；
# 如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
# 请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
# move(n, a, b, c)
# 例如，输入 move(2, 'A', 'B', 'C')，打印出：
# A --> B
# A --> C
# B --> C
def hanoi(n, a, b, c):
    if n == 1:
        print a, '-->', c
    else:
        hanoi(n -1, a, c, b)
        print a, '-->', c
        hanoi(n - 1, b, a, c)
#hanoi(1, 'A', 'B', 'C')
#hanoi(3, 'A', 'B', 'C')
#hanoi(4, 'A', 'B', 'C')

# 练习7：请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
def greet(x='world'):
    print 'Hello ' + x
greet('Jace')
greet()


# 练习8：请编写接受可变参数的 average() 函数。
def average(*args):
    sum = 0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)
print average(1, 2, 3, 4.0)
print average()


# 练习9
def city_country(CityName, Country):
    return CityName + ', ' + Country

print city_country('Shanghai', 'China')

# 练习10
l = ['Jace', 'Tom', 'Jack']
list1 = l[:]
print list1