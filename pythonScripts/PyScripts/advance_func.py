from functools import partial

def add(x, y, z):
    return x + y + z

print(add(10, 20, 5))
print(add(10, 20, 43))

myadd = partial(add, x=10, y=20)  # 将add函数的两个参数值固定后，起个新名
print(myadd(z=6))
