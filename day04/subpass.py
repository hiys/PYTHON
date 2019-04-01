#!/usr/bin/env  python3
import	 sys, subprocess, random, string

print('\033[31;40;1m__name__  is %s  sys.argv is  %s\033[0m' \
% (__name__,sys.argv))

all_chs =string.digits + string.ascii_letters

def  gen_pass(n = 8):
  result = ''
  
  for i in range(n):
    ch = random.choice(all_chs)
    result += ch
  return  result

def   add_user(username,password,fname):
  info = '''user's information ------
   username: %s
   password: %s\n'''

  subprocess.call('useradd %s' % username,shell=True)
  subprocess.call(\
    'echo  %s |passwd  --stdin  %s' % \
    (password,username),shell = True  \
  )
  
  with open(fname, 'a') as  fobj:
    fobj.write(info % (username,password))

if __name__ == '__main__':

  print('\033[30;43;1m sys.argv[0]  is %s \033[0m' % sys.argv[0])
  username = sys.argv[1]
  password = gen_pass()
  print('username is  %s  password  is %s' % (username,password))
  fname = '/tmp/users.txt'

  add_user(username,password,fname)


