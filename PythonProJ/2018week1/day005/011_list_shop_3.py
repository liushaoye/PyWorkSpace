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

shop_cart = []

salary = input("请输入您的本金:")

if salary.isdigit():
	salary = int(salary)
	while True:
		for i, v in enumerate(product_list, 1):
			print(i, '----', '品名', v[0], '----', "价格", "$", v[1])
		choice = input("请您选择购买商品的序号(退出:q):")
		if choice.isdigit():
			choice = int(choice)
			if 0 < choice <= len(product_list):
				p_iterm = product_list[choice - 1]
				if p_iterm[1] < salary:
					salary -= p_iterm[1]
					shop_cart.append(p_iterm)
				else:
					print("余额不足,还剩%s" % salary)
				print(p_iterm)
			else:
				print("编码不存在")
		elif choice.__eq__("q"):
			print("------------您已购买商品如下-------------------")
			for i in shop_cart:
				print(i)
			print("余额%s" % salary)
			break
		else:
			print("非法输入")
