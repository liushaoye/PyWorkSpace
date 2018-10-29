# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 0029 22:11
# @Author  : 北极的大企鹅！！
# @FileName: 006_Print_Format_1.py
# @Software: PyCharm


print('\n')
print('**********格式化输出,字符串类型,打印退休年龄*************   \n')

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

msg = '''
--------- info of %s --------
Name: %s
Age : %d
Job : %s
Salary: %s
You will be retired in %s years
-------- end ----------
''' % (name, name, age, job, salary,65-age)

print(msg)
