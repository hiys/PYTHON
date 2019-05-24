import time

def add():
    result = 0
    for i in range(80000000):
        result += i
    return result

start = time.time()
for i in range(2):
    print(add())
end = time.time()
print(end - start)
