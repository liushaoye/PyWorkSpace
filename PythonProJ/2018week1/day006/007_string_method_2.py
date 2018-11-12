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
print('********** 字符串操作 2 操作 *************   \n')


# 内置方法

s = 'hello cat'

# 统计元素个数
print(s.count('l'))

# 字符串首字母大写
print(s.capitalize())

print('\n')
# 居中打印
print(s.center(50,'-'))
print('\n')
# 以---结尾的
print(s.endswith('t'))
print('\n')
# 以-----开头的
print(s.startswith('h'))
print('\n')
# 转化空格
st='y\tellow'
print(st.expandtabs(tabsize=10))
print('\n')
# 查找到第一个元素，并将索引值返回
print(s.find('c'))
# 复制变量
stt='I am {name}'
print(stt.format(name='tom'))
print('\n')
# 变量为字典
sdd='I am {name}, I am {age} years old'
print(sdd.format_map({'name':'wangwu','age':19}))
print('\n')
# index 找不到会报错
print(s.index('c'))
# 是不是字符串
print('abc'.isalnum())
# 是不是十进制的数
print('7777'.isdecimal())
print(s.encode())
# 返回是一个数
print('555555'.isdigit())
# 是不是一个数
print('55555'.isnumeric())
# 命名是否规范
print('adsfsd'.isidentifier())
# 必须小写
print('ABc'.islower())
# 必须大写
print('ADC'.isupper())
# 是否是个空格
print(' '.isspace())
# 标题首字母大写判断
print('Hello Mike'.istitle())
# 所有大写转小写
print('zGGGGGG'.lower())
# 所有小写变大写
print('dfasdf'.upper())
# 大写变小写，小写变大写
print('Hello'.swapcase())




