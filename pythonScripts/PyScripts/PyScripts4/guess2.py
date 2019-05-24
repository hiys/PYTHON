import random

num = random.randint(1, 10)  # 随机生成一个10以内的数字
running = True

while running:
    result = int(input("guess the number: "))

    if result > num:
        print('猜大了')
    elif result < num:
        print('猜小了')
    else:
        running = False
        print('猜对了')

print(num)
