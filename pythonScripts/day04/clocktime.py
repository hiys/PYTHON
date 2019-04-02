#!/usr/bin/env  python3
import  time, sys

print('\033[31;47;1m__name__ is %s sys.argv  is %s\033[0m' \
% (__name__,sys.argv))

def  carriageReturn():
  for  i   in  range(1,7):
    print('\033[%d;40;1m*%d\033[0m' % (i+30,i),end = '')
    sys.stdout.flush()
    time.sleep(0.1)
  
  print('\n#注意"\r"13回车回到行首不换行，"\n"10回车直接进入下一行')
  
  for i in range(1,7):  #注意"\r"13回车回到行首不换行，"\n"10回车直接进入下一行
    print('\033[%d;40;1m\r*%d\033[0m' % (i+30,i),end = '')
    sys.stdout.flush()
    time.sleep(0.2)
  print()

def  rail():
  print('#' * 10,end='')
  n, loop = 0,0

  while True:
    if  n == 11:
      n = 0
      loop += 1
    if loop == 3:
      print('Successful installation####')
      break
    print('\033[%d;47;1m\r%s@\033[0m%s' % (n+26,'#' * n, '#' * (10-n)),end='')
    sys.stdout.flush()
    time.sleep(1.1)
    n += 1

  print()

if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0] is %s\033[0m' % sys.argv[0])
  
  carriageReturn()
  rail()
