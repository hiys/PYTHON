#!/usr/bin/env  python3
import	 sys, subprocess, random, string, getpass

print('\033[31;40;1m__name__  is %s  sys.argv is  %s\033[0m' \
% (__name__,sys.argv))


userdb = {}
def register():
  username = input('username: ')
# 使用in和not in判断 "键username" 是否存在于字典userdb中
  if username in userdb:
    print('\033[31;1m%s already exists.\033[0m' % username)
  else:
    password = input('password: ')
    userdb[username] = password

def login():
  username = input('username: ')
  password = getpass.getpass('password: ')
  # if username not in userdb or userdb['username'] != password:
#对字典userdb 中的键username , 返回它对应的值password,
#如果字典中不存在此键username , 则返回默认设置的值'not found'
  print('\033[30;43;1mReal password is %s\033[0m' \
         % userdb.get(username,'not found'))

  if userdb.get(username,'not found') != password:
    print('\033[31;1mLogin incorrect\033[0m')
  else:
    print('\033[32;1mLogin successful\033[0m')

def show_menu():
  prompt = """  (0) register
  (1) login
  (2) quit
Please input your choice(0/1/2): """

  cmds = {'0': register, '1': login}
  print('把函数register, login 都存在字典cmds里面了%s' % cmds)
  while True:
    choice = input(prompt).strip()[0]
    if choice not in '012':
      print('Invalid choice. Try again.')
      continue
    if choice == '2':
      print('Look forward to seeing you next time !')
      break
    cmds[choice]()


if __name__ == '__main__':

  print('\033[30;43;1m sys.argv[0]  is %s \033[0m' % sys.argv[0])
  show_menu()


