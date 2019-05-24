# 列表解析：用于生成列表
alist = [20]
blist = [20 + 10]
clist = [20 + 10 for i in range(5)]
dlist = [20 + i for i in range(1, 6)]
elist = [20 + i for i in range(1, 11) if i % 2 == 0]
iplist = ['192.168.1.%s' % i for i in range(1, 255)]
strlist = ['hello world', '2nd line', ' abc']
newlist = ['%s\n' % line for line in strlist]

