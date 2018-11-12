#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://www.mrliu.com
@software: PyCharm
@file: 006_string_method_1.py
@time: 2018/11/11 20:35


# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

print('\n')
print('********** 字符串操作 3 操作 *************   \n')


# 左为基准右添加
print('Hello'.ljust(50,'-'))
# 右为基准左添加
print('Hello'.rjust(60,'*'))
# 开头结尾换行符去掉
print('\npppp\t'.strip())
# 左边换行空格去除
print('    ppp\t\n'.lstrip())
# 右边换行空格去除
print('    ppp\t\n'.rstrip())

# 替换字段中的内容
print('my book'.replace('oo','ee'))

# 查找功能
print('my book'.rfind('b'))

# 字符串分割
print(' my book '.split(' '))

# 右分割一次
print('myobook'.rsplit('o',1))

# title 首字母大写
print("it's the title".title())

# 返回指定长度的字符串。
print("it's the title".zfill(20))

