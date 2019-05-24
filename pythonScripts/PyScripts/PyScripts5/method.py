class A:
    def foo(self):
        print('in A')

    def bar(self):
        print('in A-bar')

class B(A):
    def foo(self):
        print('in B')

class C(A):
    def foo(self):
        print('in C')

class D(C, B):   # 继承是自下向上，自左向右查找属性
    pass

if __name__ == '__main__':
    d = D()
    d.foo()
    d.bar()
