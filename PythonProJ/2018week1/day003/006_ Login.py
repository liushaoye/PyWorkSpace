# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 0031 23:05
# @Author  : 北极的大企鹅！！
# @FileName: 006_ Login.py
# @Software: PyCharm


print('\n')
print('********** 登录功能 *************   \n')

_user = "zhangsan"

_password = "123456"



for i in range(3):
	username = input("账户:")
	password = input("密码:")
	
	if username.__eq__(_user) and password.__eq__(_password):
		print("登陆成功")
		break
	else:
		print("重新输入用户名或密码")
print("退出")
