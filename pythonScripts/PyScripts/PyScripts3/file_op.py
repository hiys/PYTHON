with open('mima') as fobj:    # with语句结束，文件自动关闭
    print(fobj.readline())

# data = fobj.read()   无法在关闭的文件上执行读操作
