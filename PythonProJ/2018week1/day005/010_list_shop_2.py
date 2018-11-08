# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 0006 20:04
# @Author  : 北极的大企鹅！！
# @FileName: 008_list_other_4.py
# @Software: PyCharm


print('\n')
print('**********购物车编写 数组方式输出*************   \n')

product_list = [
	('Mac', 9000),
	('Kindle', 800),
	('Tesla', 900000),
	('python book', 105),
	('bike', 2000),
]

salary = input("请输入您的本金:")

if salary.isdigit():
	salary = int(salary)
	for i in  enumerate(product_list) :
		print(i[0]+1,i[1][0],"价格","$",i[1][1])
