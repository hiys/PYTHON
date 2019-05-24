import time
import os
import sys

def add():
    result = 0
    for i in range(80000000):
        result += i
    return result

start = time.time()
for i in range(2):
    pid = os.fork()
    if not pid:
        print(add())
        sys.exit()
os.waitpid(-1, 0)
os.waitpid(-1, 0)
end = time.time()
print(end - start)
