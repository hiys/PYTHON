#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
TCP协议 用主机的IP地址 加上 主机上的端口号 作为 TCP连接的端点，
   这种 端点 就叫做  套接字（socket） 或 插口。
使用给定的地址族，套接字类型 和 协议号来创建一个新套接字对象
#>>> socket.IPPROTO_RAW
#255
#>>> socket.IPPROTO_IP
#0
#>>> socket.IPPROTO_ICMP
#1
#>>> socket.IPPROTO_TCP
#6
#>>> socket.IPPROTO_UDP
#17
"""

import  sys, socket

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

class  TcpTimeClient:
  def  __init__(self, serverhost, serverport):
    "注意主机ip是字符串类型str , 服务器端口号是整数类型int"
##第一步：建立socket对象
#使用给定的地址族，套接字类型 和 协议号来创建一个新套接字
#socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
    self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP )
    print('客户端socket对象是---- \n%s\n---type(self.client_sock) is %s' \
       %  (self.client_sock, type(self.client_sock)))

##第二步：绑定服务端的ip地址和服务端端口, 链接服务器,连接服务器
    self.server_addr = (serverhost, serverport)  #作为一个元组类型的数据
    self.client_sock.connect(self.server_addr)


#第3-4步,处理阶段，服务器与客户端通过send和recv方法通信(传输数据)
#调用套接字self.client_sock 与 服务器通信
  def  communicate(self) :
    while  True:
      '''communicate (与某人)交流(信息或消息、意见等)'''
  #第三步: 发送数据到服务器
      try:
        clientdata_str = input('\n客户端输入信息:')
      except  KeyboardInterrupt:
        print('\n#用户ctrl+ c 中断执行^C 报错')
        break
      print('----*%s*----\n' % clientdata_str)
#----**----
#----*	*----  
      clientdata_bytes = bytes(clientdata_str, encoding= 'utf8')
      print('--clientdata_bytes --*%s*----\n' % clientdata_bytes) 
#--clientdata_bytes --*b''*----
#--clientdata_bytes --*b'\t'*----

      self.client_sock.sendall(clientdata_bytes)
      
      if  not  clientdata_str.strip():#若客户端输入任意连续空字符(含\v\t 空格)
        break
  #第4 步,接收服务端的数据
      fromserver_databytes = self.client_sock.recv(1024) #接收服务端信息，一次接收数据的大小最多是1024字节
  
      print('接收的服务端[二进制]信息是\n %s \n type is --**--%s' %  ([fromserver_databytes],type(fromserver_databytes)))
  
      server_datastr =  str(fromserver_databytes, encoding='utf8') #将服务器发送的二进制文字转utf8字符串格式
      print('\n注意如果服务器执行 Ctrl + C会发生二进制文字转换错误UnicodeDecodeError\n')
      print('---接受的服务器---信息转utf8字符串格式\n', server_datastr, end ='')

    #第5步,传输结束，关闭链接
    self.client_sock.close() #关闭客户端链接


#python3   tcp_client_oop.py     192.168.0.10  11200

if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  clientobj = TcpTimeClient(sys.argv[1], int(sys.argv[2]))
  clientobj.communicate()



