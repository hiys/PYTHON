# 石头/剪刀/布　人机交互小游戏。计算机随机出拳，人从键盘输入。
import random

computer = random.choice(['石头', '剪刀', '布'])
player = input("请出拳(石头/剪刀/布): ")

# print("Your choice:", player, ", Computer's choice:", computer)
# "%s...%s" % (aaa, bbb)
print("Your choice: %s, Computer's choice: %s" % (player, computer))
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('You WIN!!!')
    else:
        print('You LOSE!!!')
elif player == '剪刀':
    if computer == '石头':
        print('You LOSE!!!')
    elif computer == '剪刀':
        print('平局')
    else:
        print('You WIN!!!')
else:
    if computer == 'You WIN!!!石头':
        print('')
    elif computer == '剪刀':
        print('You LOSE!!!')
    else:
        print('平局')