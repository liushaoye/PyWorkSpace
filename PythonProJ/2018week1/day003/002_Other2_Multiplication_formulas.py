# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "liuya"
__mtime__ = "2018-01-04"
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓ ┏┓
┏┛┻━━━┛┻┓
┃ ☃ ┃
┃ ┳┛ ┗┳ ┃
┃ ┻ ┃
┗━┓ ┏━┛
┃ ┗━━━┓
┃ 神兽保佑 ┣┓
┃　永无BUG！ ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫ ┃┫┫
┗┻┛ ┗┻┛
"""


print('\n')
print('**********乘法口诀表  版本 2*************   \n')


for i in range(1, 10):
	for j in range(1, 10 - i):
		#7个空格
		print(end="       ")
	for z in range(1, i + 1):
		produce = i * z
		print("%d*%d=%2d" % (i, z, produce), end=" ")
	print(" ")

