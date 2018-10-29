# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 0029 22:11
# @Author  : 北极的大企鹅！！
# @FileName: 006_Print_Format_1.py
# @Software: PyCharm


print('\n')
print('**********格式化输出,字符串类型*************   \n')

name = input("Name:")
age = input("Age:")
job = input("Job:")
salary = input("Salary:")

msg = '''
--------- info of %s --------
Name: %s
Age : %s
Job : %s
Salary: %s
-------- end ----------
''' % (name, name, age, job, salary)

print(msg)
