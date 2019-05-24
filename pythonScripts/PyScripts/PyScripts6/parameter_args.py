def get_args(*args):  # *表示args是个元组
    print(args)

def get_age(name, age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    get_args('zhangsan')
    get_args('zhangsan', 25)
    get_args(('zhangsan', 25, 'male'))
    info = ['bob', 25]
    get_age(*info)  # *表示把序列对象拆开，得到个体
