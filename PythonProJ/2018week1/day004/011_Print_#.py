# coding=utf-8


print('\n')
print('**********while循环输出的直接三角形*************   \n')


line = 5

while line > 0 :
	temp = line
	while temp > 0:
		print("*",end="\t")
		temp -= 1
	print()
	line -= 1