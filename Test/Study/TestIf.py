#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 9:53
# @Author  : iszhang
# @Email   : 
# @File    : TestIf.py
# @software: PyCharm

# 例1
usersList = ['Admin', 'Ada', 'Jace']
if len(usersList) == 0:
    print 'We need to find some users!'
else:
    for user in usersList:
        if user == 'Admin':
            print 'Hello ' + user + ', would you like to see a status report?'
        else:
            print 'Hello ' + user + ', thank you for logging in again'

# 例2
current_users = ['Admin', 'Ada', 'Jace', 'Alice', 'Jack', 'Luce']
new_users = ['Ada', 'Mark', 'Tom', 'Jace', 'Lee']

for user in new_users:
    if user in current_users:
        print user + ' is already used!'
    else:
        print 'The ' + user + ' is available!'



