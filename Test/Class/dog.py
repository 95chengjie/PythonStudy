#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 16:20
# @Author  : iszhang
# @Email   : 
# @File    : dog.py
# @software: PyCharm

class Dog():
    """
    一次模拟小狗的简单尝试
    """
    def __init__(self, name, age):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age

    def site(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print self.name.title() + " rolled over"