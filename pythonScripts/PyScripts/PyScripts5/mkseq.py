import random

alist = list()  # 生成空列表
blist = list('abc123') # 将字符串转换为列表
clist = list(('hello', 'greet', 'welcome')) # 将元组转换成列表
atuple = tuple()  # 生成空元组
btuple = tuple('abc123')
ctuple = tuple(['hello', 'greet', 'welcome'])
astr = str(123)  # 将数字转换成字符串

num_list = [random.randint(1, 100) for i in range(10)]
print(num_list)
print(max(num_list))
print(min(num_list))

