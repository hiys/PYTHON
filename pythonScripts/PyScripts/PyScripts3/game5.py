import random

all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
cdict = {'a': '石头', 'b': '剪刀', 'c': '布'}
prompt = """(a) 石头
(b) 剪刀
(c) 布
Please input your choice(a/b/c): """

computer = random.choice(all_choice)
key = input(prompt)
player = cdict[key]

print("Your choice: %s, Computer's choice: %s" % (player, computer))
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
