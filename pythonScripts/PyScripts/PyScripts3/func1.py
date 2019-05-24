def foo():
    bar()
    print('in-foo')

# foo()   报错，foo调用bar，但是bar还不存在

def bar():
    print('in-bar')

if __name__ == '__main__':
    foo()

