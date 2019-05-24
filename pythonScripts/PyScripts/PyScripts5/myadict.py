adict = {'name': 'bob', 'age': 25}
print(len(adict))
print('bob' in adict)   # False
print('name' in adict)  # True
print(adict['name'])    # bob
adict['name'] = 'Bob'
print(adict)
adict['email'] = 'bob@tedu.cn'
print(adict)
