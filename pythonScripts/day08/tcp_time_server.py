#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
TCP协议 用主机的IP地址 加上 主机上的端口号 作为 TCP连接的端点，
   这种 端点 就叫做  套接字（socket） 或 插口。
套接字用（IP地址：端口号）表示
套接字 是网络通信过程中端点的抽象表示，
   包含进行网络通信必需的五种信息：
连接使用的协议，
本地主机的IP地址，
本地进程的协议端口，
远程主机的IP地址，远程主机进程的协议端口"""

import  sys, socket, time

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())

host_allip = ''    #空字符串''代表本机的所有ip 地址
port = 11200   #使用大于 1024的值作为端口号
addr = (host_allip, port)  #作为一个元组类型的数据

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

##第一步：建立socket对象
#使用给定的地址族，套接字类型 和 协议号来创建一个新套接字
#socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP )
print('服务器socket对象 is ---- %s \n---type(s) is %s' % (s, type(s)))
#服务器socket对象 is ---- <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('0.0.0.0', 0)> 
#---type(s) is <class 'socket.socket'>




##第二步：设置socket选项
#最后一个参数value 代表 True  或者 False
#设置地址重用,程序结束后可以再次运行
#这里value设置为 1 ，
#表示将SO_REUSEADDR标记为TRUE，
#操作系统会在服务器socket被关闭或服务器进程终止后
#马上释放该服务器的端口，
#否则操作系统会保留几分钟该端口。

s.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEADDR, 1)


#第三步：绑定socket

s.bind(addr)  #绑定主机ip地址 和 端口号


#第4 步：侦听连接

s.listen(2)   #启动监听ip地址端口, 最多有2 个客户端连接请求



#第 5 步: 阻塞等待链接请求s.accept()
#服务器通过 新的socket对象cli_sock 与客户端通信

cli_sock, cli_addr = s.accept() #阻塞等待客户端的链接请求


print('socket套接字对象cli_sock是  ', cli_sock)
#socket套接字对象cli_sock是   <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('192.168.1.10', 11200), raddr=('192.168.1.11', 59656)>


print('Client address is cli_addr connect from :\n ', cli_addr)
#Client address is cli_addr connect from :
#  ('192.168.1.11', 59656)


#第六步,处理阶段，服务器与客户端通过send和recv方法通信(传输数据)
#调用新链接对象cli_sock 与客户端cli_addr 或者服务器通信
#客户端V1 发送信息
#你好服务端 I am V1 1.11

databytes = cli_sock.recv(1024) #接收客户端信息，一次接收数据的大小最多是1024字节

print('接受的客户端信息是\n', [databytes])
#服务端V0 socket对象cli_sock  接收的客户端信息是
#  [b'\xe4\xbd\xa0\xe5\xa5\xbd\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xab\xaf I am V1 1.11\r\n']

datastr = str(databytes, encoding='utf8')  #将二进制文字转utf8字符串格式

data = '[%s] %s' % (date, datastr)


#服务端V0 socket对象cli_sock 发送二进制信息bytes(data, encoding='utf8')

serverV0 = cli_sock.sendall(bytes(data, encoding='utf8'))
#客户端V1 收到服务端socket对象cli_sock 发送的信息
#[2019年*04月*15日 14时:20分:34秒] 你好服务端 I am V1 1.11


print('cli_sock.sendall()--serverV0 返回信息---\n%s----%s' %  (type(serverV0), serverV0))
#cli_sock.sendall()--serverV0 返回信息---
#<class 'NoneType'>----None


#第七步,传输结束，关闭链接

cli_sock.close() #关闭客户端链接
s.close()    #关闭 服务端(本地主机)链接



if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)




