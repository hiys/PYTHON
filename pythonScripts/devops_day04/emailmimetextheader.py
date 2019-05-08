#!/usr/bin/env  python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8
[root@room9pc01 devopsday04]# grep  -n  Student  /etc/passwd
41:Student:x:1000:1000::/home/Student:/bin/bash

[root@room9pc01 devopsday04]# ls  /home/Student/
Desktop
[root@room9pc01 devopsday04]# ls  -ld  /home/Student/Desktop/
drwxr-xr-x 2 Student Student 4096 4月   8 10:55 /home/Student/Desktop/
[root@room9pc01 devopsday04]# id   Student
uid=1000(Student) gid=1000(Student) 组=1000(Student)
#  -M, --no-create-home		不创建用户的主目录
[root@room9pc01 devopsday04]# useradd  -M  peri
[root@room9pc01 devopsday04]# echo  1 |passwd   --stdin   peri
>>> smtplib.
smtplib.CRLF                      smtplib.SMTP_SSL(
smtplib.LMTP(                     smtplib.SMTP_SSL_PORT
smtplib.LMTP_PORT                 smtplib.bCRLF
smtplib.OLDSTYLE_AUTH             smtplib.base64
smtplib.SMTP(                     smtplib.copy
smtplib.SMTPAuthenticationError(  smtplib.datetime
smtplib.SMTPConnectError(         smtplib.email
smtplib.SMTPDataError(            smtplib.encode_base64(
smtplib.SMTPException(            smtplib.hmac
smtplib.SMTPHeloError(            smtplib.io
smtplib.SMTPNotSupportedError(    smtplib.quoteaddr(
smtplib.SMTPRecipientsRefused(    smtplib.quotedata(
smtplib.SMTPResponseException(    smtplib.re
smtplib.SMTPSenderRefused(        smtplib.socket
smtplib.SMTPServerDisconnected(   smtplib.ssl
smtplib.SMTP_PORT                 smtplib.sys
>>> 
[root@room9pc01 devopsday04]# cat   /var/mail/Student 
[root@room9pc01 devopsday04]# cat   /var/spool/mail/Student 
[root@room9pc01 devopsday04]# cat   /var/spool/mail/peri 
[root@room9pc01 devopsday04]# > /var/mail/peri 
[root@room9pc01 devopsday04]# > /var/mail/root
[root@room9pc01 devopsday04]# >/var/spool/mail/peri 
[root@room9pc01 devopsday04]# >/var/spool/mail/root 
[root@room9pc01 devopsday04]# ll  /var/spool/mail/{peri,root}
-rw-rw---- 1 peri mail 0 5月   8 17:18 /var/spool/mail/peri
-rw------- 1 root mail 0 5月   8 17:18 /var/spool/mail/root
[root@room9pc01 devopsday04]# mail  -uroot
No mail for root
>>>
"""
import  sys, smtplib, getpass
from   email.mime.text  import  MIMEText
from   email.header     import  Header

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#plain 表示纯文本文件#message 信息对象（dict 对象）
content = """
<div>
 主体内容</br>
 发送者Student
 #接收者root
 #接收者root, peri 地址
</div>
"""
message = MIMEText(content, 'plain', 'utf8')
#Content-Type: text/plain; charset="utf8"
#MIME-Version: 1.0
#Content-Transfer-Encoding: base64

print(message, type(message), sep= '\n---------\n', end='\n-------- message --------\n')
#CjxkaXY+CiDkuLvkvZPlhoXlrrk8L2JyPgog5Y+R6YCB6ICFU3R1ZGVudAogI+aOpeaUtuiAhXJv
#b3QKICPmjqXmlLbogIVyb290LCBwZXJpIOWcsOWdgAo8L2Rpdj4K
#---------
# <class 'email.mime.text.MIMEText'>
#-------- message --------

message['From']= Header('Student', 'utf-8')  #头部中的发送者Student
message['To'] = Header('root', 'utf-8')  #头部中的接收者root
subject = 'Subject邮件SMTP标题'         #头部中的主题信息
message['Subject'] = Header(subject, 'utf-8')

sender = 'Student@qq.com'    #发送者Student发送地址
receivers = ['root@localhost', 'peri@localhost']  #接收者root, peri 地址列表

#smtp_obj = smtplib.SMTP([host [, port [, local_hostname]]])
#创建SMTP对象也可以不给定参数,之后再通过对象的其他方法进行绑定

smtpobj = smtplib.SMTP('127.0.0.1')  #创建SMTP对象
print('smtpobj = ', smtpobj, end=' ---- smtpobj------\n')
#smtpobj =  <smtplib.SMTP object at 0x7f08a3d73400> ---- smtpobj------
 
print(type(smtpobj))
#<class 'smtplib.SMTP'>

#smtplib.SMTP.sendmail(from_addr,to_addrs,msg[,mail_opPons,rcpt_opPons])
smtpobj.sendmail(sender, receivers, message.as_string()) ## 发送邮件




print('=================   ==================\n')


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)




