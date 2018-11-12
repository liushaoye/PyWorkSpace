# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 0012 11:16
# @Author  : 北极的大企鹅！！
# @FileName: 010_Three_Linkage.py
# @Software: PyCharm


print('\n')
print('********** 三级菜单 *************   \n')

msg = '''
--------- message --------
   要求:
	1、打印省、市、县三级菜单
	2、可返回上一级
	3、可随时退出程序
--------------------------
'''

print(msg)

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


exit_flag = False
current_layer = menu

layers = [menu]

while not  exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "b":
        current_layer = layers[-1]
        #print("change to laster", current_layer)
        layers.pop()
    elif choice not  in current_layer:continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[choice]

