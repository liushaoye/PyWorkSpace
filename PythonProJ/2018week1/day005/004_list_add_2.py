# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 0005 11:19
# @Author  : 北极的大企鹅！！
# @FileName: 004_list_add_2.py
# @Software: PyCharm


print('\n')
print('**********数组练习 exercise 3 *************   \n')

a = ['万达', '张三', '李四', '龙五', '赵六', '孙七', '周八', '吴九', '郑十']

####################添加 append \ insert
# 末尾加元素
# a = a.append('刘一')
# print(a)

# 固定位置添加元素(开启2,需要注释上边的)
# a.insert(1, '陈二')
# print(a)

###################修改

##赋值方式修改数据
# a[0] = '刘一';
# print(a)

##多个修改方式

# a[0:1]={'刘一','陈二'}
# print(a)


###############删除  remove pop del

# remove 列表方式
#
# a.remove('张三')
#
# print(a)
#
# # remove 列表方式二
#
# a.remove(a[0])
#
# print(a)


# #pop 通过索引的方式删除
#
# a.pop(0)
# print(a)


# del 删除某个对应值

del a[1]
print(a)

# 删除整个对象

# del a
# # 报错a不存在
# print(a)
