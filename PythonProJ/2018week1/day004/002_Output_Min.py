# coding=utf-8

print('\n')
print('**********输出最小值*************   \n')


number_1 = int(input("输入第一个数"))
number_2 = int(input("输入第二个数"))
number_3 = int(input("输入第三个数"))

min_number = 0

if number_1 < number_2:
	min_number = number_1
	if min_number < number_3 :
		print("最小值是:", min_number)
	else:
		print("最小值是:",number_3)
else:
	min_number = number_2
	if min_number < number_3 :
		print("最小值是:", min_number)
	else:
		print("最小值是:", number_3)








