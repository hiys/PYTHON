adict = {}
bdict = dict()

print(adict)
print(bdict)

cdict = {'username': 'bob', 'password': '123'}
ddict = dict([['username', 'bob'], ['password', 'abc']])

print(ddict)

edict = {}.fromkeys(['bob', 'alice'], 7)
print(edict)

for key in ddict:
    print("%s: %s" % (key, ddict[key]))

print("%(username)s: %(password)s" % ddict)

ddict['username'] = 'tom'
print(ddict)

ddict['email'] = 'tom@tedu.cn'
print(ddict)

print(ddict.pop('email'))
ddict.clear()
print(ddict)

fdict = cdict.copy()  # 只把cdict的内容复制给fdict
print(id(cdict))      # 两个字典使用不同的内存空间
print(id(fdict))

print(cdict.get('username', 'not found'))
print(cdict.get('phone', 'not found'))

cdict.setdefault('username', 'alice')  # 如果username是字典的key，不更新
cdict.setdefault('qq', '1234')  # 如果qq不是字典的key，将其加入到字典
# ----------------------------

adict = {'username': 'bob', 'qq': '123456'}
print(adict.items())
print(adict.keys())
print(adict.values())
bdict = {'email': 'bob@tedu.cn'}
adict.update(bdict)
print(adict)
