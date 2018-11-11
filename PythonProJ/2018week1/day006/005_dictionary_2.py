#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://www.mrliu.com
@software: PyCharm
@file: 003_dictionary.py
@time: 2018/11/11 14:39


# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

print('\n')
print('********** 字典操作 3 其他操作 *************   \n')


# 创建字典数组
d1=dict.fromkeys(['host1','host2','host3'],'Mac')
print(d1)


# 字典嵌套

av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
print(av_catalog["大陆"]["1024"])
print('\n')

av_catalog["欧美"]["www.youporn.com"][1] ="好"
print(av_catalog)

# 排序 根据键，字符串是ACS排序
dic={5:'555',2:'222',4:'444'}
print(sorted(dic))

# 值排序
print(sorted(dic.values()))
print("\n")

# 字典遍历
dic5 = {'name': 'alex', 'age': 18}

# 效率更高
for i in dic5:
	print(i, dic5[i])
	
for items in dic5.items():
	print(items)
	
# 效率低
for keys, values in dic5.items():
	print(keys, values)
print("\n")

# 封装字典
dic={'zhangsan':{'age':23,'sex':'male'},
     '李四':{'age':33,'sex':'male'},
     'wangwu':{'age':27,'sex':'women'}
     }

for i in dic:
	print(i, dic[i])











