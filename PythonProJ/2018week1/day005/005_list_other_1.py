# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 0005 11:19
# @Author  : 北极的大企鹅！！
# @FileName: 004_list_add_2.py
# @Software: PyCharm


print('\n')
print('**********数组练习 其他操作 *************   \n')

a = ['to', 'be', 'or', 'not', 'to', 'be']

#### count
print(a.count("to"))
print('\n')

#### extend 方法可以在列表的末尾一次性追加另一个序列中的多个值

a = [1, 2, 3]

b = [4, 5, 6]

# a 放入b 组中
a.extend(b)

print(a)

print('\n')

#### index 方法用于从列表中找出某个值第一个匹配项的索引位置：

a = ['刘一', '陈二', '张三', '李四', '王五', '赵六', '孙七', '周八', '吴九', '郑十']

##输出角标值,元素重复以第一个值为输出
print(a.index('李四'))

print('\n')

####取得角标值重复的数据的值
a = ['刘一', '陈二', '张三', '李四', '王五', '张三', '赵六', '孙七', '周八', '吴九', '郑十']

#取出第一个角标值
first_flag = a.index('张三')

#切片操作
little_index = a[first_flag + 1:]

#取第二个在小列表位置
second_flag = little_index.index('张三')


#通过列表一和列表二计算其位置
big_index = first_flag + second_flag +1

final_index = big_index

print("key =",final_index,",","value =",a[final_index])
print()

print('\n')
