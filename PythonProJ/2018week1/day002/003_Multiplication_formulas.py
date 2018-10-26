# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "liuya"
__mtime__ = "2017-12-17"
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

#####################乘法口诀表 ######################

print('\n')
print('**********乘法口诀表*************   \n')

for i in range(1, 10):
	for j in range(1, i + 1):
		print("%d*%d=%2d" % (i, j, i * j), end=" ")
	print('')
