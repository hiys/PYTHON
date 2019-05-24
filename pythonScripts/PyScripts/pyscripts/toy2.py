class BearToy:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def sing(self, song):
        print(song)

class NewBearToy(BearToy):   # 新类是BearToy的子类
    def sing(self):  # 父子类有相同的方法，子类覆盖父类的方法
        print('aaa...bbb...ccc')

    def run(self):
        print("I can run.")

if __name__ == '__main__':
    b1 = NewBearToy('middle', 'brown')
    b1.sing()
    b1.run()
    b2 = BearToy('large', 'orange')
    b2.sing('lalalala...')
