# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 0029 22:11
# @Author  : 北极的大企鹅！！
# @FileName: 006_Print_Format_1.py
# @Software: PyCharm


print('\n')
print('**********格式化输出,判断输入价格,不符合转为符合*************   \n')

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

# 长的像不像数字,比如200d , '200'
if salary.isdigit():
	salary = int(salary)
else:
	
	exit("must input digit") #退出程序

msg = '''
--------- info of %s --------
Name: %s
Age : %d
Job : %s
Salary: %s
You will be retired in %s years
-------- end ----------
''' % (name, name, age, job, salary, 65 - age)

print(msg)
