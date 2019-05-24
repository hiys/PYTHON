# range(1, 11, 2)   生成的数字，包括起始值，不包括结束值，最后是步长值
print(range(5))
print(list(range(5)))   # [0, 1, 2, 3, 4]
for i in range(5):
    print(i)

print(list(range(11, 21)))  # 11 - 20
print(list(range(1, 11, 2)))  # 10以内的奇数
print(list(range(10, 0, -1)))  # 从10到1
