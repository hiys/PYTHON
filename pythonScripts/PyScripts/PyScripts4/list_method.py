# alist = [10, 20, 'bob', 'alice', [1, 2, 3]]
# print(len(alist))
#
# alist[-1] = 100
# print(alist)
#
# alist[2:4] = ['tom', 'jerry']
# print(alist)
#
# alist[1:1] = [12, 14, 16, 18] # 在数字10后面加上4个数字
# print(alist)

alist = [10, 20, 'bob', 'alice']
alist.append(30)  # 在尾部追加
alist.insert(1, 15) # 在下标为1的位置写入15
alist.count(10)  # 统计10在列表中出现的次数
alist.index(20)  # 返回20的下标
alist.pop()  # 移除列表中最后一项，并将它返回
alist.pop(2) # 移除下标为2的项
alist.remove('bob')  # 把bob从列表中移除
blist = [10, 15, 14, 16, 18, 20]
blist.sort()  # 列表排序
blist.reverse() # 翻转
clist = blist.copy()  # 只将值从blist拷贝到clist
clist.clear()  # 清空列表
blist.extend(['bob', 'alice', 'jack'])  # 向blist中写入三项值


