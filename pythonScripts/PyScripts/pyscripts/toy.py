class Manufacture:
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email

    def update_phone(self, newph):
        # 调用发邮件的方法
        self.phone = newph

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def update_email(self, newem):
        self.email = newem

# factory = Manufacture('13322334455', 'xxx@tedu.cn')
# print(factory.get_phone())

class BearToy:
    def __init__(self, size, color, phone, email):
        self.size = size
        self.color = color
        self.factory = Manufacture(phone, email)

    def sing(self, song):
        print(song)

if __name__ == '__main__':
    tidy = BearToy('small', 'orange', '13322334455', 'xxx@tedu.cn')
    tidy.sing('lalala...')
    print(tidy.factory.get_phone())
    print(tidy.factory.get_email())

