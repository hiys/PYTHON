#!/usr/bin/env  python3
import	 sys, subprocess, random, string

print('\033[31;40;1m__name__  is %s  sys.argv is  %s\033[0m' \
% (__name__,sys.argv))

stack = []

def  testpy():
  pass  


def push_it():
  item = input('item to push:')
  stack.append(item)
  print('\033[31;47;1mstact is %30s\033[0m' %  stack )

def pop_it():
  if stack:
    print('\033[32;1m Popped %s \033[0m' % stack.pop())
  else:
    print('\033[31;40;1m Empty stack\033[0m')
  print('\033[30;43;1mstact is %-30s\033[0m' %  stack )

def view_it():
  print('\033[32;1m %s\033[0m' % stack)

def  show_menu():
  prompt = '''  (0) push_it
  (1)pop_it
  (2)view_it
  (3)quit
Please input your choice(0|1|2|3):'''

  cmds = {'0':push_it,'1':pop_it, '2':view_it}
  print('把函数push_it, pop_it, view_it 都存在字典cmds里面了%s' % cmds)
  while True:
    choice = input(prompt).strip()[0]
    print('\033[30;43;1mchoice  is----%-10s\033[0m' %  choice)
    if choice not in '0123':
      print('Invalid input,try again')
      continue #结束本次循环,进入下一次循环
    if choice == '3':
      break

    cmds[choice]()
  #    if choice == '0':
  #      push_it()
  #    elif  choice == '1':
  #      pop_it()
  #    elif  choice == '2':
  #      view_it()



if __name__ == '__main__':

  print('\033[30;43;1m sys.argv[0]  is %s \033[0m' % sys.argv[0])
  show_menu()

