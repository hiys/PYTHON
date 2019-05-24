import os
import sys

def hello():
    print('hello world!')

for i in range(5):
    pid = os.fork()
    if pid == 0:
        hello()
        sys.exit()
