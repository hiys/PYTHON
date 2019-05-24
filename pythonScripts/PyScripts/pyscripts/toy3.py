class BearToy:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def sing(self, song):
        print(song)

class NewBearToy(BearToy):   # 新类是BearToy的子类
    def __init__(self, size, color, material):
        # BearToy.__init__(self, size, color)  # 非绑定方法
        super(NewBearToy, self).__init__(size, color)
        self.material = material

    def run(self):
        print("I can run.")

if __name__ == '__main__':
    b1 = NewBearToy('middle', 'brown', 'fur')
    b1.run()

