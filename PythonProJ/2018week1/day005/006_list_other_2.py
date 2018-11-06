# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 0005 11:19
# @Author  : 北极的大企鹅！！
# @FileName: 004_list_add_2.py
# @Software: PyCharm


print('\n')
print('**********数组练习 其他操作 2 *************   \n')

####  reverse 方法将列表中的元素反向存放。

a = ['刘一', '陈二', '张三', '李四', '王五', '赵六', '孙七', '周八', '吴九', '郑十']

##输出角标值,元素重复以第一个值为输出
a.reverse()

print(a)

print('\n')

#### sort 方法用于在原位置对列表进行排序。
x = [4, 6, 2, 1, 7, 9]

x.sort()

print(x)

print('\n')

#### sort 字符也可以排序,按照ASC编码顺序排序

a = ['刘一', '陈二', '张三', '李四', '王五', '赵六', '孙七', '周八', '吴九', '郑十']

a.sort()

print(a)

print('\n')

#### 结合排序
x = [4, 6, 2, 1, 7, 9]
x.reverse()
x.sort()

print(x)

print('\n')

#### 简化排序

x = [4, 6, 2, 1, 7, 9]

x.sort(reverse=True)

print(x)

print('\n')






