#!/usr/bin/env python3
#! -*- coding:utf8 -*-
'''
  元组是序列类型，有数字下标，每一项没有类似字典的key键名
  注意命名的元组，比普通元组多了一个功能，可以给每个元组元素起名，类似字典key键名
'''
import  collections

p1 = (10, 11, 20, 30)
#注意前后2个Point要保持一致,注意大小写
Point = collections.namedtuple('Point', ['x', 'x1','y', 'z'])
P2 = Point(100,110, 220, 333)
print('P2[0]= %d\n'  % P2[0])
print('P2[1]= %d\n'  % P2[1])
print('P2[2]= %d\n'  % P2[2])
print('P2[1:]=%s  type(P2[1:])=%s\n' % ( str(P2[1:]), type(P2[1:])))

print(P2.x, type(P2.x), end=' ----P2.x\n\n')
print(P2.y,  end=' ----P2.y\n\n')
print(P2.z,  end=' ----P2.z\n\n')

#[root@V1 myansi]# python3   ntupletest.py
#P2[0]= 100
#
#P2[1]= 110
#
#P2[2]= 220
#
#P2[1:]=(110, 220, 333)  type(P2[1:])=<class 'tuple'>
#
#100 <class 'int'> ----P2.x
#
#220 ----P2.y
#
#333 ----P2.z

#[root@V1 myansi]# pyflakes   ntupletest.py
#[root@V1 myansi]# type  pyflakes 
#pyflakes 已被哈希 (/usr/local/bin/pyflakes)
#[root@V1 myansi]# ll   /usr/local/bin/pyflakes
#-rwxr-xr-x 1 root root 222 5月  21 12:49 /usr/local/bin/pyflakes
#[root@V1 myansi]# file   /usr/local/bin/pyflakes
#/usr/local/bin/pyflakes: Python script, ASCII text executable
#
#[root@V1 myansi]# cat   -n   /usr/local/bin/pyflakes
#     1 #!/usr/local/bin/python3.6
#     2 # -*- coding: utf-8 -*-
#     3 import re
#     4 import sys
#     5  
#     6 from pyflakes.api import main
#     7    
#     8 if __name__ == '__main__':
#     9    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
#    10    sys.exit(main())

