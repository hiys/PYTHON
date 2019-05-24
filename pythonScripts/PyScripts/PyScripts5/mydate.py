class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    @classmethod    # 用于创建类方法
    def create_date(cls, string_date):  # cls表示类本身而不是实例
        year, month, date = map(int, string_date.split('-'))
        dt = cls(year, month, date)  # 即Date(year, month, date)
        return dt  # 将创建的实例返回

    @staticmethod
    def is_date_valid(string_date):
        year, month, date = map(int, string_date.split('-'))
        return year < 4000 and 0 < month < 13 and 0 < date < 32

if __name__ == '__main__':
    d1 = Date(2018, 3, 25)
    d2 = Date.create_date('2018-04-01')
    print(d2.year, d2.month, d2.date)
    print(Date.is_date_valid('2020-20-02'))
    if Date.is_date_valid('2020-10-02'):
        d3 = Date.create_date('2020-10-02')
        print('create instance done')
    else:
        print('Invalid date format.')

