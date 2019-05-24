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
print('done')
