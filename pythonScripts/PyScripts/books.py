class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '<Book: %s>' % self.title

    def __call__(self):
        print('《%s》 is written by %s.' % (self.title, self.author))

if __name__ == '__main__':
    pybook = Book('Core Python', 'Weysley')
    print(pybook)  # 调用__str__
    pybook()   # 调用__call__
