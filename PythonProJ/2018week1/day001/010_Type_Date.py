# coding=utf-8
#!/usr/bin/python3


str1 = 'Runoob'

print(str1)  # 输出字符串
print(str1[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str1[0])  # 输出字符串第一个字符
print(str1[2:5])  # 输出从第三个开始到第五个的字符
print(str1[2:])  # 输出从第三个开始的后的所有字符
print(str1 * 2)  # 输出字符串两次
print(str1 + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义