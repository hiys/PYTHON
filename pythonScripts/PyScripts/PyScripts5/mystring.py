print('tom said: "hello word!"')
print("tom's pet is a cat")
words = "hello\ngreet\nnice"
print(words)   # \n会被转义为回车输出
new_words = '''hello
welcome
greet'''
print(new_words)

py_str = 'Python'
print(len(py_str))  # len()用于取出长度
print(py_str[0])  # 索引经常称作下标，从0开始
# print(py_str[6])   # 报错
print(py_str[-1])   # 自右向左的下标从-1开始
print(py_str[2:4])  # 取切的时候起始下标对应的字符包含，结束的不包含
print(py_str[2:])   # 结束下标没写，表示到结尾
print(py_str[:2])
print(py_str[:])    # 从开头到结尾
print(py_str[::2])  # 从开头到结尾，步长为2
print(py_str[::-1])  #　步长为负，从右向左取
print('t' in py_str)
print('th' in py_str)
print('to' in py_str)  # to不是连续出现，所以返回False
print('to' not in py_str)
print(py_str + ' is good.')
print('*' * 30)
