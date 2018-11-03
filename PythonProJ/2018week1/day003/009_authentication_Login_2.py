# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 0031 23:46
# @Author  : 北极的大企鹅！！
# @FileName: 007_foot_for.py
# @Software: PyCharm


print('\n')
print('********** 登录功能完善 - version 2 for 后跟else *************   \n')

_user = "zhangsan"

_password = "123456"

for i in range(3):
	username = input("账户:")
	password = input("密码:")
	
	if username.__eq__(_user) and password.__eq__(_password):
		print("登陆成功")
		passed_authentication = True
		break
	else:
		print("重新输入用户名或密码")
else:
	print("输入错误三次,登录失败,三分钟后重新登录")
