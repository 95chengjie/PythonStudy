#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 16:26
# @Author  : iszhang
# @Email   : 
# @File    : Test.py
# @software: PyCharm

from Class.dog import Dog
from Restaurant import Restaurant

dog = Dog('willie', 6)
print dog.name.title()

dog.site()

restaurant = Restaurant('AA', 'BB')
restaurant.describe_restaurant()
restaurant.open_restaurant()