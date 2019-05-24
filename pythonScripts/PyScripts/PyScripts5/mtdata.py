import threading
import time

a = 10

def add1():
    global a
    time.sleep(2)
    a = a + 5
    print('in add1 a is', a)

def add2():
    global a
    time.sleep(2)
    a = a + 100
    print('in add2 a is', a)

t1 = threading.Thread(target=add1)
t2 = threading.Thread(target=add2)
t1.start()
t2.start()
t1.join() # 等到t1结束之后，主线程才会继续向下执行
t2.join()
print('a =', a)

# 在运行时主线程、t1、t2同时执行，所以运行多次t1/t2看到的a的值不一样
