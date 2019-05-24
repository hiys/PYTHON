import random

all_chs = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

result = ''
for i in range(8):
    ch = random.choice(all_chs)
    result += ch

print(result)
