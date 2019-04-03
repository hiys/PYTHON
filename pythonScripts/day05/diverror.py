#!/usr/bin/env  python3
import	 sys, subprocess, random, string, getpass

print('\033[31;47;1m__name__  is %s  sys.argv is  %s\033[0m' \
% (__name__,sys.argv))

def  solution_error():
  try:
    num = int(input("please enter an integer:"))
    result = 100 / num
    
    print('\033[32;46;1m 100/num is %f\033[0m' % result, \
    end= ' this is result\n')
  except  ValueError:
    print('数据类型错误,或者是空输入,请输入整数')
  except  ZeroDivisionError:
    print('数字0 不能使用,除数不能是零!')
  except  KeyboardInterrupt:
    print('#用户ctrl+ c 中断执行^CTraceback 报错')
  except  EOFError:
    print('#敲快捷键ctrl+d 中断输入,会报异常')


def  solution_error2():
  try:
    num = int(input("please enter an integer:"))
    result = 100 / num
    
    print('\033[32;46;1m 100/num is %f\033[0m' % result, \
    end= ' this is result\n')
  except  Exception:
    print('ValueError, ZeroDivisionError, EOFError')
  except  KeyboardInterrupt:
    print('#用户ctrl+ c 中断执行^CTraceback 报错')


def  solution_error3():
  try:
    num = int(input("please enter an integer:"))
    result = 100 / num
    
    print('\033[32;46;1m 100/num is %f\033[0m' % result, \
    end= ' this is result\n')
  except  (ValueError, ZeroDivisionError, EOFError):
    print('\nValueError, ZeroDivisionError, EOFError')
  except  KeyboardInterrupt:
    print('\n#用户ctrl+ c 中断执行^CTraceback 报错')


def  solution_error4():
  try:
    num = int(input("please enter an integer:"))
    result = 100 / num
    
  except  (ValueError, ZeroDivisionError, EOFError):
    print('\nValueError, ZeroDivisionError, EOFError')
  except  KeyboardInterrupt:
    print('\n#用户ctrl+ c 中断执行^CTraceback 报错')

  print('\033[32;46;1m 100/num is %f\033[0m' % result, \
    end= ' this is result\n')


if __name__ == '__main__':

  print('\033[30;43;1m sys.argv[0]  is %s \033[0m' % sys.argv[0])
#  solution_error()
#  solution_error2()
#  solution_error3()
  solution_error4()



