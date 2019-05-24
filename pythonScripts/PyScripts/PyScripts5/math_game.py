import random

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    cmds = {'+': add, '-': sub}  # 将函数存入字典
    nums = [random.randint(1, 100) for i in range(2)] # 生成两个数
    nums.sort(reverse=True)  # 降序排列
    op = random.choice('+-')
    result = cmds[op](*nums)  # 调用存入字典的函数，把nums列表拆开，作为参数传入
    prompt = "%s %s %s = " % (nums[0], op, nums[1])

    for i in range(3):
        try:
            answer = int(input(prompt))
        except:
            continue

        if answer == result:
            print('你真棒，答对了！')
            break  # 答对了就不要再回答了，结束循环
        else:
            print('答错了')
    else:
        print("%s%s" % (prompt, result))   # 只有循环不被break才执行


def main():
    while True:
        exam()
        try:
            go_on = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            go_on = 'n'

        if go_on in 'nN':
            print('\nBye-bye.')
            break


if __name__ == '__main__':
    main()
