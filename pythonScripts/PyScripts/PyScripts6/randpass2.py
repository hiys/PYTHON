import random
import string

all_chs = string.digits + string.ascii_letters


def gen_pass(n=8):
    result = ''

    for i in range(n):
        ch = random.choice(all_chs)
        result += ch

    return result


if __name__ == '__main__':
    print(gen_pass())
    print(gen_pass(4))
