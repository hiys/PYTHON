try:
    num = int(input("number: "))
    result = 100 / num
except ValueError:
    print('请输入数字')
except ZeroDivisionError:
    print('不允许使用0')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
else:
    print(result)  # 不发生异常才执行的语句
finally:
    print('Done')  # 不管异常是否发生都要执行的语句

print('end of program')
