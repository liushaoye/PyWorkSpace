# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 0029 22:34
# @Author  : 北极的大企鹅！！
# @FileName: 010_Other_Format.py
# @Software: PyCharm

print('\n')
print('**********格式化输出,打印整数*************   \n')
print("I am %d years old." %(25))


print('\n')
print('**********格式化输出,打印浮点数*************   \n')
print ("His height is %f m"%(1.70))

print('\n')
print('**********格式化输出,打印浮点数保留两位*************   \n')
print ("His height is %.2f m"%(1.70))

print('\n')
print('**********格式化输出,打印指定占位符宽度*************   \n')
print ("Name:%10s Age:%8d Height:%8.2f"%("Alfred",25,1.70))


print('\n')
print('**********格式化输出,打印指定占位符*************   \n')
print ("Name:%-10s Age:%08d Height:%08.2f"%("Alfred",25,1.70))


print('\n')
print('**********格式化输出,打印科学计数法*************   \n')

print(format(0.0026,'.2e'))