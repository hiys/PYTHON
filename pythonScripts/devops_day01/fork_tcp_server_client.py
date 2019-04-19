#!/usr/bin/env   python3
#coding:UTF-8
"""#coding=UTF-8
#•  父进程通过os.wait()来得到子进程是否终止的信息
#•  在子进程终止和父进程调用wait()之间的这段时间,
#子进程被称为zombie(僵尸)进程
#•  os.waitpid()的返回值:
#如果子进程尚未结束则返回0, <class 'tuple'> *** (0, 0)
#如果子进程已经结束了,
 就返回子进程的PID, <class 'tuple'> *** (6273, 0)
"""

import  sys, socket, os, time

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

def  invoke():
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return   '%s ----**** %f' %  (date, time.time())

serhost = ''    #空字符串''代表本机的所有ip 地址
serport = 11200   #使用大于 1024的值作为端口号
seraddr = (serhost, serport)  #作为一个元组类型的数据

#第一步：建立socket对象
#socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP )
print('服务器socket对象ser ---- %s\n---type(ser) is %s\n' % (ser, type(ser)))


##第二步：设置socket选项
ser.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEADDR, 1)


###第三步：绑定socket
ser.bind(seraddr)  #绑定主机ip地址 和 端口号


#第4 步：侦听连接
ser.listen(2)   #启动监听ip地址端口, 一次最多同时有2 个客户端连接请求


while  True:
  try:
    while  True:
#•  waitpid()接受两个参数,
#第一个参数 设置为 -1, 表示与wait()函数相同;
#第二个参数 设置为 os.WNOHANG 是os模块的常量= 1 表示不挂起父进程

      result_tuple = os.waitpid(-1, os.WNOHANG)
      print('os.waitpid(-1, os.WNOHANG)的返回值是元组类型的数据, \
      result_tuple = %s \n' %  str(result_tuple) )

      if  result_tuple[0] == 0:  #子进程尚未结束,返回0
        break

  #OSError 是system错误/ChildProcessError 是子进程错误

  except OSError as ose : 
    print('\nError : ', ose)

  #第 5 步: 阻塞等待链接请求s.accept()
  #服务器通过 新的socket对象cli_sock 与客户端通信
  
  print('正在等待待客户端的链接请求ser.accept()----------\n')
  
  cli_sock, cli_addr = ser.accept() #阻塞等待客户端的链接请求

  print('新的套接字对象cli_sock是  ', cli_sock)
  print('本次连接的客户端ip地址和端口号  ', cli_addr)


  pid = os.fork()   #父进程 生成 子进程

  print('产生的子进程pid号是 %d  数据类型是%s\n' %  (pid, type(pid)))

  if  pid: ##子进程已经结束了, 返回子进程的PID号,这里是父进程执行的程序
    cli_sock.close() #第七步:关闭客户端链接
    print('已经关闭客户端链接')

  else: #子进程pid= 0, 尚未结束,返回0,这里是子进程代码区
----------------????????????????????

  #第六步,处理阶段，服务器与客户端通过send和recv方法通信(传输数据)
  
  #服务器通过 新的socket对象cli_sock接收字节信息
  
  databytes = cli_sock.recv(1024) #接收客户端信息，一次接收的数据最多是1024字节
  
  
  #将客户端发送的二进制文字转 utf8 字符串格式
  datastr = str(databytes, encoding='utf8') 
  
  print('\n接收的客户端信息转utf8字符串格式--> ', datastr)
  
  send_data = '[%s] %s' % (invoke(), datastr) #服务端处理客户端发来的信息
  print('\n服务端将要发送的信息---', send_data )
  
  #服务端调用新链接对象cli_sock 发送
  #二进制信息bytes(send_data, encoding='utf8')给客户端
  
  cli_sock.sendall(bytes(send_data, encoding='utf8'))
  
  cli_sock.close() #第七步:关闭客户端链接


#第 八 步,传输结束，关闭服务端socket对象ser
ser.close()    #关闭 服务端(本地主机)链接



if  __name__ == '__main__':
  sys.stdout.write('\n\033[31;47;1msys.argv is %s\n\n\033[0m' % sys.argv)  




