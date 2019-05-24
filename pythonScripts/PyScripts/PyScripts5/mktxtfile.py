# 首先，在脑海里想像一下，程序是如何运行的
# 接着，思考一下程序有哪些功能，半这些功能定义成函数，这样就可以把复杂的
# 问题简单化，编写某一个函数的时候，不用考虑其他函数的功能
# 然后，编写程序框架
# 最后，向框架内部写入具体代码
import os

def get_fname():
    while True:
        filename = input('请输入文件名：')
        if not os.path.exists(filename):
            break
        print('%s 已存在，请重试。' % filename)

    return filename


def get_contents():
    contents = []

    print('请输入内容，结束请输入end。')
    while True:
        line = input('> ')
        if line == 'end':
            break
        contents.append(line)

    return contents


def wfile(fname, contents):
    with open(fname, 'w') as fobj:
        fobj.writelines(contents)


if __name__ == '__main__':
    fname = get_fname()
    contents = get_contents()
    contents = ['%s\n' % line for line in contents]
    wfile(fname, contents)
