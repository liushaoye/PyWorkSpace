# coding=utf-8


print('\n')
print('**********while循环按照输入输出图形*************   \n')




width =int(input("请输入长度值:"))
height =int(input("请输入宽度值:"))


height_num = 1
while  height_num <= height:
	width_num = 1
	while width_num <= width:
		print("#",end="\t")
		width_num += 1
	print()
	height_num += 1

