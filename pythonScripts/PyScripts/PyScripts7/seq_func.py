alist = [10, 46, 22, 3, 85, 72]
print(sorted(alist))   # 返回一个新的列表，不会改变原始列表内容
print(alist)

print(reversed(alist))  # 反转列表，返回一个对象
print(list(reversed(alist)))
for i in reversed(alist):
    print(i)
