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
print('********** 字符串操作 1 操作 *************   \n')


# 创建字符串，内部有单引号的时候外部用双引号

s = 'hello cat'

s_1 = " Let's go"


print(s+'\n'+s_1)


# 多次输出

print('hello world' * 20+'\n')

# 通过索引去取

print('helllllll0'[3:]+'\n')

# 判断在不在
print('e2l' in 'hello'+'\n')

# 格式化输出

print('aex is a good teacher'+'\n')
print('%s is a good teacher'%'aex'+'\n')

# 字符串拼接

a = '123456'
b = 'abcdcd'
d = '789456'

c = '----'.join([a,b,d])
print(c+'\n')




