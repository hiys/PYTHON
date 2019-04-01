#!/usr/bin/env  python3
import	 sys, subprocess, random, string

print('\033[31;40;1m__name__  is %s  sys.argv is  %s\033[0m' \
% (__name__,sys.argv))

all_chs =string.digits + string.ascii_letters

def  get_contents():
  contents = []
  print('input contents end with end: ')
  while True:
    line = input('input> ')
    if  line == 'end':
      break
    contents.append(line)
  print(' contents  is  %s' % contents)
 # contents = ['%s\n' % line for line in contents]
 # print('last printed contents\n  %s' % contents)
  return  contents


if __name__ == '__main__':

  print('\033[30;43;1m sys.argv[0]  is %s \033[0m' % sys.argv[0])
  
  contents = get_contents()
  print('+%s+' % ('*' * 28))
  for  line in  contents:
    print('+{0:-^28}+'.format(line))
  print('+%s+' % ('*' * 28))



