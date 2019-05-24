# 集合：无序，直接，有可变和不可变两种集合，不可变类型的数据才能成为集合元素
# 集合也用{}，像是一个无值的字典
aset = set('hello')  # 可变 {'h', 'e', 'l', 'o'}
bset = frozenset('hello') # 不可变
cset = set(['hello', 'world'])  # {'hello', 'world'}

print(len(aset))
for ch in aset:
    print(ch)
# ----------------
aset = set('abc')   # {'b', 'a', 'c'}
bset = set('cde')
print(aset & bset)  # 交集
print(aset | bset)  # 并集
print(aset - bset)  # 差补，元素只在aset中，不在bset中
aset.add('new')  # {'b', 'a', 'c', 'new'}
aset.update('new') # {'a', 'b', 'e', 'c', 'w', 'n', 'new'}
aset.update(('hello', 'world'))
aset.remove('hello') # 移除hello
#----------------
aset = set('abcde')
bset = set('cde')
bset.issubset(aset)  # bset是aset的子集
aset.issuperset(bset)  # aset是bset的超集
aset.union(bset)   # 并集
aset.intersection(bset) # 交集
aset.difference(bset)  # 差补
