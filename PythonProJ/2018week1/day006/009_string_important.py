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
print('********** 字符串操作重点 *************   \n')

# 重点需要记住的

# 1、统计元素个数
s = 'hello cat'
print(s.count('l'))

# 2、居中打印
s2 = 'hello cat'
print(s2.center(50, '-'))

# 3、以-----开头的
s3 = 'hello cat'
print(s3.startswith('h'))

# 4、查找到第一个元素，并将索引值返回
s4 = 'hello cat'
print(s4.find('c'))

# 5、赋值变量
stt = 'I am {name}'
print(stt.format(name='tom'))

# 6、所有大写转小写
print('zGGGGGG'.lower())

# 7、所有小写变大写
print('dfasdf'.upper())

# 8、开头结尾换行符去掉
print('\npppp\t'.strip())

# 9、替换字段中的内容
print('my book'.replace('oo','ee'))

# 10、字符串分割
print(' my book '.split(' '))
