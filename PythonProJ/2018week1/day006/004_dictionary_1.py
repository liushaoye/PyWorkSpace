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
print('********** 字典操作 2 *************   \n')


# 添加数组

dic1 = {'name' : 'zhangdan'}
dic1['age'] = 18
print(dic1)

# 列表转换
print(list(dic1.keys()))

# 取值
print(list(dic1.values()))


# 改 update
names_class2 = {1:'张三',2: '李四',3: '王五', 4:'赵六','age':16}
names_class3 = {5:'wusir', 6:'alvin'}
names_class2.update(names_class3)
print(names_class2)

# 删，索引方式
print(names_class2.pop(1))
print(names_class2)


# 删除指定键值对

del names_class2["age"]
print(names_class2)

# 随机删除某组键值对，并以元组方式返回值
a = names_class2.popitem()
print('随机删：-',a,names_class2)


# 删除整个字典
del  names_class2
try:
	print(names_class2)
except 	NameError:
	print('已删除不存在了')





















