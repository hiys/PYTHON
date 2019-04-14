#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8 专门为版本2 解决默认编码问题,可以识别中文

TCP协议 用主机的IP地址 加上 主机上的端口号 作为 TCP连接的端点，
   这种 端点 就叫做  套接字（socket） 或 插口。
套接字用（IP地址：端口号）表示
套接字 是网络通信过程中端点的抽象表示，
   包含进行网络通信必需的五种信息：
连接使用的协议，
本地主机的IP地址，
本地进程的协议端口，
远程主机的IP地址，远程主机进程的协议端口"""

import  sys, socket

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

host_allip = ''    #空字符串''代表本机的所有ip 地址
port = 11200   #使用大于 1024的值作为端口号
addr = (host_allip, port)  #作为一个元组类型的数据

#        基于网络的 套接字       socket.AF_INET
#        面向连接的 套接字类型为    SOCK_STREAM
#使用给定的地址族，套接字类型 和 协议号来创建一个新套接字
#socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
#协议号通常为零 0 ,  可以省略,

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
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP )


##第二步：设置socket选项
#setsockopt(level, optname, value)函数
#  用于任意类型、任意状态套接口的设置选项值
#第一个参数level 为 协议层 参数,指明了希望访问一个选项所在的协议栈
#socket.SOL_SOCKET  来访问套接口层选项
#socket.SOL_TCP     来访问TCP层   选项

#第二个参数optname 是与第一个参数 level 相对应的
#第二个参数optname 决定了 该协议层下 选项组合
#SO_REUSEADDR参数的作用是
#   当socket关闭后，本地端用于该socket的端口号立刻就可以被重用

#最后一个参数value 代表 True  或者 False
#设置地址重用,程序结束后可以再次运行
#这里value设置为 1 ，
#表示将SO_REUSEADDR标记为TRUE，
#操作系统会在服务器socket被关闭或服务器进程终止后
#马上释放该服务器的端口，
#否则操作系统会保留几分钟该端口。

##第二步：设置socket选项
s.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEADDR, 1)


#第三步：绑定socket
#S.bind((host,port))，其中host为服务器ip，通常为空，
#也可以绑定到一个特定的ip地址。
#Port为端口号
#addr = (host_allip, port)

s.bind(addr)  #绑定主机ip地址 和 端口号


#第4 步：侦听连接
#listen()函数进行侦听连接,
#指明了在服务器实际处理连接的时候，允许有多少个等待的"连接请求"在队列中等待
#操作系统可以挂起的最大连接数量,该值至少为1，大部分应用程序设为5

#接到连接请求后，这些请求必须排队等候连接，如果队列已满，则拒绝请求

s.listen(2)   #启动监听ip地址端口, 最多有2 个客户端连接请求



#第 5 步: 阻塞等待链接请求s.accept()
#当某个客户端连接的时，
# accept方法会返回一个含有两个元素的元组( cli_sock,  cli_addr )
#第一个元素是新的连接客户端socket套接字对象 = cli_sock 
#服务器通过 新的socket对象cli_sock 与客户端通信
#第二个元素是 客户端的ip地址 和 端口号信息 = cli_addr

cli_sock, cli_addr = s.accept() #阻塞等待客户端的链接请求


#[root@V1 ~]# ifconfig  eth1 |head -2
#eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#        inet 192.168.1.11  netmask 255.255.255.0  broadcast 192.168.1.255
#
#[root@V1 ~]# telnet   192.168.1.10   11200
#Trying 192.168.1.10...
#Connected to 192.168.1.10.
#Escape character is '^]'.

print('socket套接字对象cli_sock是  ', cli_sock)
#socket套接字对象cli_sock是   <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('192.168.1.10', 11200), raddr=('192.168.1.11', 59656)>


print('Client address is cli_addr connect from :\n ', cli_addr)
#Client address is cli_addr connect from :
#  ('192.168.1.11', 59656)


#第六步,处理阶段，服务器与客户端通过send和recv方法通信(传输数据)
#调用新链接对象cli_sock 与客户端cli_addr 或者服务器通信

#[root@V1 ~]# telnet   192.168.1.10   11200
#................
#haha I am  V1  telnet   192.168.1.10   11200----------
#Connection closed by foreign host.
#[root@V1 ~]# 

data = cli_sock.recv(1024) #接受客户端信息，一次接收数据的大小最多是1024字节

print('接受的客户端信息是\n', [data])
#接受的客户端信息是
# [b'haha I am  V1  telnet   192.168.1.10   11200----------\r\n']


#第七步,传输结束，关闭链接

cli_sock.close() #关闭客户端链接
s.close()    #关闭 服务端(本地主机)链接



if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)




