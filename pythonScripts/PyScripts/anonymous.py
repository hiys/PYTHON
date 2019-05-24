# 高阶函数: 函数的参数也是函数
from random import randint

def func1(n):
    return n % 2

def func2(n):
    return n * 2 + 1

def func3(x, y):
    return x + y

if __name__ == '__main__':
    num_list = [randint(1, 100) for i in range(10)]
    print(num_list)
    a = filter(func1, num_list)
    print(list(a))
    for i in filter(lambda n: n % 2, num_list):
        print(i)

    print(list(map(func2, num_list)))
    print(list(map(lambda n: n * 2 + 1, num_list)))
