#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 16:07
# @Author  : iszhang
# @Email   : 
# @File    : FileReader.py
# @software: PyCharm

# 1、读取文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print contents.rstrip()

# 2、逐行读取
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print line.rstrip()

# 3、创建一个包含文件内容的列表
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print line.rstrip()

# 4、使用文件的内容
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

# 5、写文件
file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write('I like Linux\n')
    file_object.write('I like C\n')

# 6、附加模式
file_name = 'programming.txt'
with open(file_name, 'a') as file_object:
    file_object.write('I like C++\n')