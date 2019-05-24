import random

num = random.randint(1, 10)  # 随机生成一个10以内的数字
counter = 0

while counter < 5:
    result = int(input("guess the number: "))

    if result > num:
        print('猜大了')
    elif result < num:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter += 1
else:   # 注意, else属于while语句，当循环正常结束时执行，如果
    print(num)  # while被break，就不执行了
