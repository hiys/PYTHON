# 进程：加载到内存中的一系列指令
# 以前写的程序都是单进程，单线程
# 父子进程都有自己独立的运行空间
# 线程运行于进程内部，多个线程共享进程的运行空间

import os

a = 10
pid = os.fork()
if pid:
    a += 10
    print('in parent, a is %d' % a)
else:
    a += 100
    print('in child, a is', a)
