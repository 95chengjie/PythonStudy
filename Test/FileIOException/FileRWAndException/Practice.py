#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 16:58
# @Author  : iszhang
# @Email   : 
# @File    : Practice.py
# @software: PyCharm

# 1、提示用户输入其名字，然后写入name.txt中
name = raw_input("请输入姓名：")
with open('name.txt', 'a') as file_object:
    file_object.write(name)

# 2、编写一个while循环，提示用户输入其名字。用户输入其名字后，在屏幕上显示一条问候语，并将一条访问记录添加到文件 guest_book.txt中，确保这个文件中的每条记录都独占一行
flag = True
count = 3
while flag:
    name = raw_input("请输入姓名：")
    print "Hi, " + name
    with open('guest_book.txt', 'a') as guest_book:
        guest_book.write(name+'\n')
    count = count - 1
    if count == 0:
        flag = False
