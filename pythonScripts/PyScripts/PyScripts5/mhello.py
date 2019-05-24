import os

print('starting...')
os.fork()  # 分岔，父进程将自身资源完全拷贝一份，生成子进程
           # 后续代码在父子进程都要执行
print('hello world!')

