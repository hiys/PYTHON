fib = [0, 1]

# 思路是，向列表尾部追加的数据是列表最后两项之和

l = int(input("数列长度: "))
for i in range(l - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)
