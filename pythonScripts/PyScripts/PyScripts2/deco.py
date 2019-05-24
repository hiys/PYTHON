import time

def deco(func):
    def timeit():
        start = time.time()
        result = func()
        end = time.time()
        return end - start, result   # 将会返回元组
    return timeit

@deco
def loop():
    result = []
    for i in range(1, 6):
        result.append(i)
        time.sleep(0.3)
    return result

if __name__ == '__main__':
    # loop = deco(loop)
    print(loop())

