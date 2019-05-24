# 5!=5X4X3X2X1
# 5!=5X4!
# 5!=5X4X3!
# 5!=5X4X3X2!
# 5!=5X4X3X2X1!
# 1!=1

def func1(n):
    if n == 1:
        return n

    return n * func1(n - 1)
           # 5 * func1(4)
                # 4 * func1(3)

if __name__ == '__main__':
    print(func1(5))
    print(func1(6))



