# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "liuya"
__mtime__ = "2017-12-17"
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓ ┏┓
┏┛┻━━━┛┻┓
┃ ☃ ┃
┃ ┳┛ ┗┳ ┃
┃ ┻ ┃
┗━┓ ┏━┛
┃ ┗━━━┓
┃ 神兽保佑 ┣┓
┃　永无BUG！ ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫ ┃┫┫
┗┻┛ ┗┻┛
"""
'''*************** 一个有趣的猜数游戏 *************'''

print('\n')
print('**********一个有趣的猜数游戏*************   \n')

_princal_age = 56

title = input('Begin a game,please input enter:')
guess_age = 0

while guess_age != _princal_age:
    guess_age = int(input('please input your guess age >>>>>>>>>>>>>> : '))
    if guess_age > _princal_age:
        print('The result is bigger ,try again')
        print('\n')
    else:
        print('The result is smaller,try again')
        print('\n')

if guess_age == _princal_age:
    print('you are right..........')
    print('over')
    exit()
