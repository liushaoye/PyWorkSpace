# coding=utf-8

print('\n')
print('**********while循环打印*************   \n')


num_1=0


while num_1 <= 5 :
	print(num_1,end="_")
	num_2=0
	while num_2 <= 7 :
		print(num_2, end="-")
		num_2+=1
	
	num_1 += 1
	print()
