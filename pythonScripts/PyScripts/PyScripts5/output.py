import sys

name = sys.stdin.readline()  # 回车也被读入到变量中
print(name)
print('ok')
sys.stdout.write('hello world!\n')   # 标准输入
sys.stderr.write('error output.\n')  # 标准错误
