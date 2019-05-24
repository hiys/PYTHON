# GIL:全局解释器锁，某一时刻GIL只允许一个线程进入cpu处理
# 所以多线程不适合做计算密集型应用
# 多线程适合io密集型应用

import time
import threading

def add():
    result = 0
    for i in range(80000000):
        result += i
    print(result)
    return result

start = time.time()
t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(end - start)
