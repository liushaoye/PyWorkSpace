# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "liuya"
__mtime__ = "2017-12-07"
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓ ┏┓
┏┛┻━━━┛┻┓
┃ ☃ ┃
┃ ┳┛ ┗┳ ┃
┃ ┻ ┃
┗━┓ ┏━┛
┃ ┗━━━┓
┃ 神兽保佑 ┣┓
┃　永无BUG！ ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫ ┃┫┫
┗┻┛ ┗┻┛
"""

print('****************字符串测试*****************')

print('***********转义字符*****************')
print('C:\some\name')
print('\t')
print(r'c:\user\name')

print('\t')
print('str' + 'ing', 'my' * 3)

print('字符串数组的使用', '\t')
word = 'Python'
print(word[ 0 ], word[ 5 ])
print('使用方法二', '\t')
print(word[ -1 ], word[ -6 ])

print('\t')
word = 'ilovepython'
print(word[ 1:5 ])
print(word[ : ])
print(word[ 5: ])
print(word[ -10: -6])

print('\t')
