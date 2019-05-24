import os
import sys
import time

print('starting...')
pid = os.fork()  # 父进程pid值为子进程的进程号，子进程pid值为0
if pid:
    print('in parent')
else:
    time.sleep(3)
    print('in child')
    sys.exit()
# 第二个参数是１表示不挂起父进程，返回值元组中第一个数，如果子进程不是僵尸进程
# 返回０，如果是僵尸进程，返回子进程的pid。
# 一个waitpid只能处理一个子进程
# print(os.waitpid(-1, 1))
print(os.waitpid(-1, 0))    # 第二个参数是0表示挂起父进程
print('done')
