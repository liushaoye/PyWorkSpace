# coding=utf-8


print('\n')
print('**********while循环打印 9 * 9 乘法表*************   \n')

num_1 = 1

while num_1 <= 9:
	num_2 = 1
	while num_2 <= num_1:
		print("%d*%d=%2d" % (num_1, num_2, num_1 * num_2), end="\t")
		num_2 += 1
	print()
	num_1 += 1
