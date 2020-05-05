#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 11:50
# @Author  : iszhang
# @Email   : 
# @File    : Car.py
# @software: PyCharm

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.make) + str(self.model) + str(self.year)
        print long_name

car = Car('auDi', 'a4', '2016')
car.get_descriptive_name()