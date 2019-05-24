class A:
    def foo(self):
        print('A method')

class B:
    def bar(self):
        print('B method')

class C(A, B):  # 子类可以有多个父类，所有的父类方法均可继承
    pass

if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()
