class MyClass:
    count = 0   # 类属性
    def __init__(self):
        self.a = 10      # 这里的a绑定在实例上，是实例属性
        self.count += 1  #  self.count = self.count + 1
                         # 右侧的self.count没有定义，将会查类属性

if __name__ == '__main__':
    print(MyClass.count)
    mc1 = MyClass()
    print(MyClass.count)
    print(mc1.__dict__)   # oop的属性保存在__dict__字典中
    print(MyClass.__dict__)
