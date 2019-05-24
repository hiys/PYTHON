alist = ['hello', 'greet', 'welcome']

for ind in range(len(alist)):
    print('%s: %s' % (ind, alist[ind]))

print(list(enumerate(alist)))

for item in enumerate(alist):
    print('%s: %s' % (item[0], item[1]))

for ind, val in enumerate(alist):
    print('%s: %s' % (ind, val))
