class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.pages = pages

    def __str__(self):
        return "《%s》" % self.__title

if __name__ == '__main__':
    b1 = Book('Core Python', 'Weysley', 800)
    print(b1)
    print(b1.pages)
    # print(b1.__title)  # 在类的外部无法使用
    print(b1._Book__title)  # 访问私有属性的方式　
