# yn = input('Continue(y/n)? ')
#
# while yn != 'n':
#     print('running...')
#     yn = input('Continue(y/n)? ')
#
# DRY原则: Don't Repeat Yourself
# Pythonic
#
while True:
    yn = input('Continue(y/n)? ')
    if yn == 'n':
        break     # 结束循环，循环体内后续代码被跳过，但是不结束程序
    print('running...')

print('Done')
