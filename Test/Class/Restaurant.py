#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 11:32
# @Author  : iszhang
# @Email   : 
# @File    : Resturant.py
# @software: PyCharm

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print self.restaurant_name + self.cuisine_type

    def open_restaurant(self):
        print '正在营业'