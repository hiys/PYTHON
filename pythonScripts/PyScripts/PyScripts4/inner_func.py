def counter(start=0):
    count = start  # 定义局部变量count
    def incr():
        nonlocal count  # 内层函数不能直接使用外层函数的变量，需要使用nonlocal说明
        count += 1
        return count  # 返回数字
    return incr   # 外层函数返回值是内层函数

if __name__ == '__main__':
    a = counter()
    print(a())
    b = counter(10)
    print(b())
    print(a())
    print(b())
