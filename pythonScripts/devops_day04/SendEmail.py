#!/usr/bin/env  python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8
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
[root@room9pc01 devopsday04]# netstat  -npult |grep  :25 |column  -t
tcp   0  0  127.0.0.1:25  0.0.0.0:*  LISTEN  1181/master
tcp6  0  0  ::1:25        :::*       LISTEN  1181/master
>>>
"""
import  sys, smtplib, getpass
from   email.mime.text  import  MIMEText
from   email.header     import  Header

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

def  send_mail(host163, mail_pass, sender, receivers, content, subject):

  #plain 表示纯文本文件#message 信息对象（dict 对象）
  message = MIMEText(content, 'plain', 'utf8')
  #Content-Type: text/plain; charset="utf8"
  #MIME-Version: 1.0
  #Content-Transfer-Encoding: base64
  
  print(message, type(message), sep= '\n---------\n', end='\n-------- message --------\n')

  message['From']= Header(sender, 'utf-8')  #头部中的发送者'm13530503630@163.com'
  message['To'] = Header(receivers[0], 'utf-8')  #头部中的接收者'3424969110@qq.com'
  #subject 头部中的主题信息
  message['Subject'] = Header(subject, 'utf-8')
  
  #smtp_obj = smtplib.SMTP([host [, port [, local_hostname]]])
  #创建SMTP对象也可以不给定参数,之后再通过对象的其他方法进行绑定
  #smtp_obj = smtplib.SMTP()
  #smtp_obj.connect(mail_host, 25)  #25为SMTP端口号

  smtpobj = smtplib.SMTP(host163, 25)  #创建SMTP对象, 25是非SSL协议SMTP默认端口号
  print('smtpobj = ', smtpobj, end=' ======= smtpobj------\n')
  #smtpobj =  <smtplib.SMTP object at 0x7fe900f61400> ======= smtpobj------
   
  print(type(smtpobj))
  #<class 'smtplib.SMTP'>

  smtpobj.login(sender, mail_pass)
  print('=====  smtpobj.login(sender, mail_pass) ====\n')


  #sender 发送者'm13530503630@163.com' 发送地址
  #接收者 ['3424969110@qq.com', '2119793139@qq.com']  地址列表receivers  
  #smtplib.SMTP.sendmail(from_addr,to_addrs,msg[,mail_opPons,rcpt_opPons])
  smtpobj.sendmail(sender, receivers, message.as_string()) ## 发送邮件

  print('===== smtpobj.sendmail(sender, receivers, message.as_string()) ======\n')


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

  host163 = 'smtp.163.com'  #邮件服务器地址
  mailpasswd = getpass.getpass()
  sender = 'm13530503630@163.com'  #发送者邮件发送地址
  #接收者地址列表['3424969110@qq.com', '2119793139@qq.com']
#  receivers = ['3424969110@qq.com', '2119793139@qq.com'] #163不能和qq邮箱通信,有限制
  receivers = ['m13530503630@163.com']  #163只能在163邮箱账户内互相发送邮件
#  receivers = ['3424969110@qq.com'] #163不能和qq邮箱通信,有限制
  content = """
  <div>
   主体内容</br>
   发送者'm13530503630@163.com'
   #头部接收者#163不能和qq邮箱通信,有限制
   #接收者 地址列表['m13530503630@163.com']
</div>"""
  subject = 'Subject邮件SMTP标题'         #头部中的主题信息

  send_mail(host163, mailpasswd, sender, receivers, content, subject)
  print('\n---------------done well ! ----------')


