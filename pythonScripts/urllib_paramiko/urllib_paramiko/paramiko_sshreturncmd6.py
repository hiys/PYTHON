#!/usr/bin/env  python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8
>>> result = ssh.exec_command('id lisi')   #在ssh服务器上执行指定命令
>>> type(result)
<class 'tuple'>

>>> type(result[2])    # 标准错误, 类文件对象
<class 'paramiko.channel.ChannelStderrFile'>

>>> type(result[1])     #标准输出 类文件对象
<class 'paramiko.channel.ChannelFile'>

>>> type(result[0])       #标准输入  类文件对象
<class 'paramiko.channel.ChannelFile'>

>>> ssh.exec_command("ifconfig |awk '/inet /{print $2}'")[1].read().decode('utf8')
'192.168.0.13\n192.168.1.13\n127.0.0.1\n192.168.122.1\n'
>>>
"""
import  sys, os, paramiko
import  getpass, threading

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

def rcmd(hostname, cmd, passwd = None, user= 'root', port = 22):
  ssh = paramiko.SSHClient() #创建用于连接ssh服务器的实例#创建sshclient
  pkAP = paramiko.AutoAddPolicy()  #设置自动添加主机密钥

  #回答连接yes#接受不在本地 ~/.ssh/known_hosts文件下的主机ip地址
  ssh.set_missing_host_key_policy(pkAP)
  #连接ssh服务器
  ssh.connect(hostname, port, username=user, password=passwd)
  #在ssh服务器上执行指定命令
  stdin, stdout, stderr = ssh.exec_command(cmd)
  out = stdout.read()
  err = stderr.read()
  if out:
      print('[%s] OUT:\n%s' % (hostname, out.decode('utf8')))

  if err:
      print('[%s] ERROR:\n%s' % (hostname, err.decode()))
  ssh.close() #exit退出连接


print('=================   ==================\n')


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

  if  len(sys.argv) != 3:
    print('Usage: %s ipfile "shell command"' %  sys.argv[0])
    exit(1)
  pswd = getpass.getpass()
  ipfile = sys.argv[1]
  
  if not os.path.isfile(ipfile):
    print('No such file ', os.path.isfile(ipfile))
    exit(2)
  print('file existed ', os.path.isfile(ipfile))
#[root@room9pc01 urllib_paramiko]# cat  ipaddrs.txt 
#192.168.0.10
#192.168.0.11
#192.168.0.12
#192.168.0.13
#[root@room9pc01 urllib_paramiko]#
  cmd = sys.argv[2]
  with open(ipfile) as  fobj:
    for  line   in fobj:
      ip = line.strip()
      thr = threading.Thread(target= rcmd, args=(ip, cmd, pswd))
      thr.start()
      print(thr, type(thr), end = '------thr\n')    
#rcmd(hostname, cmd, user= 'root', passwd = '1', port = 22)
#      rcmd(ip, sys.argv[2], passwd= pswd)


#[root@room9pc01 urllib_paramiko]# python3  paramiko_sshreturncmd6.py  ipaddrxs.txt  "ls  /home"
#__name__ is __main__
#=================   ==================
#
#sys.argv is ['paramiko_sshreturncmd6.py', 'ipaddrxs.txt', 'ls  /home']
#Password: 
#No such file  False



