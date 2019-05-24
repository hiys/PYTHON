def gen_fib(l=10):
    fib = [0, 1]

    for i in range(l - 2):
        fib.append(fib[-1] + fib[-2])

    return fib   # 返回值，而不是打印，不返回变量名 [0, 1, 1, 2, 3]

length = int(input("数列长度: "))  # 输入10
a = gen_fib(length) # 调用函数时，将10作为参数传入，不是传入length
print(a)
with open('/tmp/fib.txt', 'w') as fobj:
    fobj.write(str(a))
