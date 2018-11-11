#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://www.mrliu.com
@software: PyCharm
@file: 003_dictionary.py
@time: 2018/11/11 14:39


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
print('********** 字典操作 *************   \n')

dictionary = {1: 'zhangsan', 2: 'lisi', 'age':36, "other":{"user": "wangwu", 'age':27}, 'is_right':True}

# 打印整个字典
print(dictionary)

# 取字典的某个值
print(dictionary['other']['user'])


# 字典两大特点：无序，键唯一，键字符相同，后一个覆盖前一个

# 其他写法
dic = {'name':'wang','age':36}
dic2 = dict([['name','zhouliu'],])
dic3 = dict((('name','zhouliu'),))
print(dic2)
print(dic3)
