#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
UDP:用户数据报协议，是一个面向无连接的协议。
采用该协议不需要两个应用程序先建立连接。
#使用给定的地址族，套接字类型 和 协议号来创建一个新套接字
#socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
## 创建UDP套接字
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
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
#s.setsockopt(level,optname,value)  :设置给定套接字选项的值
server_sock.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEADDR, 1)
#level:(级别)： 指定选项代码的类型。
#SOL_SOCKET:   基本 套接口
#IPPROTO_IP:   IPv4套接口
#IPPROTO_IPV6: IPv6套接口
#IPPROTO_TCP:  TCP 套接口
#level定义了哪个选项将被使用
#最后一个参数value 代表 True  或者 False
#设置socket.SO_REUSEADDR 地址重用,程序结束后可以再次运行
#这里value设置为 1 ，
#表示将SO_REUSEADDR标记为TRUE，
#操作系统会在服务器socket被关闭或服务器进程终止后
#马上释放该服务器的端口，
#否则操作系统会保留几分钟该端口。
"""

import  sys, socket, time

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())

server_host_allip = ''    #空字符串''代表本机的所有ip 地址
server_port = 11200   #使用大于 1024的值作为端口号
server_addr = (server_host_allip, server_port)  #作为一个元组类型的数据

##第一步：建立服务端socket对象 ## 创建UDP套接字
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

print('服务器socket对象----------\n%s\n---type(server_sock) is %s\n' \
   % (server_sock, type(server_sock)))
#服务器socket对象----------
#<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=17, laddr=('0.0.0.0', 0)>
#---type(server_sock) is <class 'socket.socket'>



##第二步：设置socket选项, 
# 设置 level 级别为 socket.SOL_SOCKET 基本套接口层
server_sock.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEADDR, 1)


#第三步：绑定服务器套接字socket
server_sock.bind(server_addr)  #绑定主机ip地址 和 端口号


#第4 步：接收数据
#socket.recvfrom(bufsize [，flags ])
#从socket接收数据。
#返回值是一个二进制数据和一个元组类型的数据，
#其中client_data_bytes 是表示接收数据的字节对象，
# client_addr (元组类型的数据) 是发送数据的套接字的地址。
#接收客户端信息，一次接收数据的大小最多是1024字节

client_data_bytes, client_addr =  server_sock.recvfrom(1024)

print(client_data_bytes, type(client_data_bytes), sep = '\n --- ', end = '---bytes\n')
#b'I am \xe5\xae\xa2\xe6\x88\xb7\xe7\xab\xafabc -- '
# --- <class 'bytes'>---bytes

print(client_addr,type(client_addr), sep = '\n --- ', end = ' ---tuple\n')
#('192.168.0.11', 51036)
# --- <class 'tuple'> ---tuple

print("\n----接收的客户端信息client_data_bytes 转utf8字符串---------")

client_data_str = str(client_data_bytes, encoding= 'utf8')
print(client_data_str,end = '\n\n')
#I am 客户端abc --

#第 5 步调用新客户端返回的ip地址 给客户端client_addr 发送信息

toClient_data_bytes = bytes(date + '--服务器信息' + client_data_str, encoding = 'utf8')

server_sock.sendto(toClient_data_bytes, client_addr)



#第 六 步:关闭服务器端的套接字
server_sock.close() 



if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)








