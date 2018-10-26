# coding=utf-8

print('\n')
print('**********输出最大值*************   \n')


number_1 = int(input("输入第一个数"))
number_2 = int(input("输入第二个数"))
number_3 = int(input("输入第三个数"))

max_number = 0

if number_1 > number_2:
	max_number = number_1
	if max_number > number_3 :
		print("最大值是:", max_number)
	elif max_number < number_3:
		print("最大值是:",number_3)
	else:
		print("相等的值:", max_number, number_3)
elif number_1 < number_2:
	max_number = number_2
	if max_number > number_3 :
		print("最大值是:", max_number)
	elif max_number < number_3:
		print("最大值是:",number_3)
	else:
		print("相等的值:", max_number, number_3)
else:
	print("相等的值:", number_1,number_2)