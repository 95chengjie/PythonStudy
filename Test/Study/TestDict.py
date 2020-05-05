#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 11:00
# @Author  : iszhang
# @Email   : 
# @File    : TestDict.py
# @software: PyCharm
# 例1
user_0 = {
    'username': 'Jace',
    'first': 'K',
    'last': 'Jace'
}
# for key, value in user_0.items():
#     print key + ' ' + value

# 例2
# aliens = []
# x = 1
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': x, 'speed': 'slow'}
#     aliens.append(new_alien)
#     x = x + 1
#
# for alien in aliens[:5]:
#     print alien

# # 例3
# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarch': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'hashell']
# }
# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         print '\n' + name.title() + "'s favorite language is " + str(favorite_languages[name][0])
#     else:
#         print '\n' + name.title() + "'s favorite language are:"
#         for language in languages:
#             print language

# 例4
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print '\nUsername: ' + username
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print '\tFull name: ' + full_name.title()
    print '\tLocation: ' + location.title()
