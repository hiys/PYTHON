class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):  # __sub__  __mul__
        return self.num + other

    def __radd__(self, other):  # __rsub__ __rmul__
        return self.num + other

    def __gt__(self, other):  # __lt__ __ge__ __le__ __ne__
        return self.num > other

    def __truediv__(self, other):
        return self.num / other

if __name__ == '__main__':
    n1 = Number(10)
    print(n1 + 5)
    print(5 + n1)
    print(n1 > 5)
    print(n1 / 3)
