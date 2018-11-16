# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 0012 11:16
# @Author  : 北极的大企鹅！！
# @FileName: 010_Three_Linkage.py
# @Software: PyCharm


print('\n')
print('********** 三级菜单 version 2*************   \n')

msg = '''
--------- message --------
   要求:
	1、打印省、市、县三级菜单
	2、可返回上一级
	3、可随时退出程序
   转化：
	1、可以一层一层的进入到所有层
	2、可以在每层返回上一层----------实现此处功能
	3、可以在任意层退出 主菜单
--------------------------
'''

print(msg)

menu = {
	'河北省': {
		'石家庄市': {
			'长安区': {},
			'桥西区': {},
			'新华区': {},
			'井陉矿区': {},
			'裕华区': {},
			'藁城区': {},
			'鹿泉区': {},
			'栾城区': {},
			'井陉县': {},
			'正定县': {},
			'行唐县': {},
			'灵寿县': {},
			'高邑县': {},
			'深泽县': {},
			'赞皇县': {},
			'无极县': {},
			'平山县': {},
			'元氏县': {},
			'赵县': {},
			'辛集市': {},
			'晋州市': {},
			'新乐市': {}
			
		},
		'唐山市': {
			'路南区': {},
			'路北区': {},
			'开平区': {},
			'丰南区': {},
			'丰润区': {},
			'曹妃甸区': {},
			'滦县': {},
			'滦南县': {},
			'乐亭县': {},
			'迁西县': {},
			'玉田县': {},
			'遵化市': {},
			'迁安市': {}
			
		},
		'秦皇岛市': {},
		'邯郸市': {},
		'邢台市': {},
		'保定市': {},
		'张家口市': {},
		'承德市': {},
		'沧州市': {},
		'廊坊市': {},
		'衡水市': {}
	},
	'辽宁省': {
		'沈阳市': {},
		'大连市': {},
		'鞍山市': {},
		'抚顺市': {},
		'本溪市': {},
		'丹东市': {},
		'锦州市': {},
		'营口市': {},
		'阜新市': {},
		'辽阳市': {},
		'盘锦市': {},
		'铁岭市': {},
		'朝阳市': {},
		'葫芦岛市': {}
		
	},
	'吉林省': {},
	'黑龙江省': {},
	'江苏省': {},
	'浙江省': {}
	
}

back_flag = False

exit_flag = False

while not back_flag and not exit_flag:
	for key in menu:
		print(key)
	choice = input(">> 1:").strip()
	if choice in menu:
		while not back_flag and not exit_flag:
			for key2 in menu[choice]:
				print(key2)
			choice2 = input(">>2:").strip()
			if choice2 == "b":
				back_flag = True
			if choice2 == "q":
				exit_flag = True
			if choice2 in menu[choice]:
				while not back_flag and not exit_flag:
					for key3 in menu[choice][choice2]:
						print(key3)
					choice3 = input(">>3:").strip()
					if choice3 == "b":
						back_flag = True
					if choice3 == "q":
						exit_flag = True
				else:
					back_flag = False
		else:
			back_flag = False
