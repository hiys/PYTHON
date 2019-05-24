def simple_generator():   # 生成器就是函数
    yield 100             # 用yield生成中间结果
    yield 'hello world'
    yield [1, 2, 3]

if __name__ == '__main__':
    a = simple_generator()
    for item in a:
        print(item)
