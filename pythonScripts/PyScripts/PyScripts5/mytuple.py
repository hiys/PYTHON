# tuple元组可以看作是不可变的列表
atuple = (10, 20, 'bob', 'alice', [100, 200])
print(len(atuple))
print(atuple[2:4])
print(20 in atuple)
print(atuple + (1000, 2000))
# atuple[-1] = 1000    元组不可变，不支持元素的改变
