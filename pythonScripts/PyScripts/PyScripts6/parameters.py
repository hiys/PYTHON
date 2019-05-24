def get_age(name, age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    get_age('bob', 23)
    get_age(23, 'bob')  # 能执行，但是不合逻辑
    get_age(age=23, name='bob')
    # get_age(age=23, 'bob')  语法错误，不允许key=val出现在后面
    # get_age(23, name='bob')  name得到了多个值
    # get_age()  # 参数不够
    # get_age('bob', 23, 100)  参数给多了
