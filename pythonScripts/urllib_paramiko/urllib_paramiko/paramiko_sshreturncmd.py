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

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

def rcmd(hostname, cmd, user= 'root', passwd = '1', port = 22):
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
      print('[%s] OUT:\n%s' % (hostname, out.decode()))
   #[V2] OUT:
   #2019年 05月 08日 星期三 11:51:19 CST
   #
   #[192.168.0.13] OUT:
   #V3

  if err:
      print('[%s] ERROR:\n%s' % (hostname, err.decode()))
   #[V1] ERROR:
   #ls: 无法访问robot/: 没有那个文件或目录
  ssh.close() #exit退出连接


print('=================   ==================\n')


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

  rcmd('V0', 'ls  robot/')
  rcmd('V1', 'ls  robot/')
  rcmd('V2', 'date')
  rcmd('192.168.0.13', 'hostname')



