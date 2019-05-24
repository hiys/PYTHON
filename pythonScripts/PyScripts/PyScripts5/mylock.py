import threading
import time

l = threading.Lock()

a = 10

def add1():
    l.acquire()   # 访问共享资源时，先请求锁
    global a
    time.sleep(2)
    a = a + 5
    print('in add1 a is', a)
    l.release()   # 操作结束后，释放锁

def add2():
    l.acquire()
    global a
    time.sleep(2)
    a = a + 100
    print('in add2 a is', a)
    l.release()

t1 = threading.Thread(target=add1)
t2 = threading.Thread(target=add2)
t1.start()
t2.start()
print('a =', a)

