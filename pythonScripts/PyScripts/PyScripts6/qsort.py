from random import randint

def qsort(data):
    data = list(data)
    if len(data) == 0 or len(data) == 1:  # 长度为0或1，直接返回
        return data

    middle = data.pop()  # 假设最后一项是中间值
    smaller = []
    larger = []

    for item in data:
        if item > middle:  # 比middle大的放到larger，否则放到smaller
            larger.append(item)
        else:
            smaller.append(item)

    return qsort(smaller) + [middle] + qsort(larger)


if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
    astr = 'qwertyuio'
    print(''.join(qsort(astr)))
    atuple = (10, 2, 34, 234, 1, 66, 88, 77)
    print(tuple(qsort(atuple)))

