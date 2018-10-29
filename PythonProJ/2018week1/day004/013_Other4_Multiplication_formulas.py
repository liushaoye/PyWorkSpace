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
print('**********乘法口诀表  版本 4*************   \n')


i = 1

while i <= 9:
	j = 1
	while j <= i :
		print(str(j) + "*" + str(i) + "=" + str(j * i) ,end="\t")
		j += 1
	print()
	i += 1
