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

server_host_allip = '192.168.0.10'    #服务器的ip 地址
server_port = 11200   #使用大于 1024的值作为端口号
server_addr = (server_host_allip, server_port)  #作为一个元组类型的数据

##第一步：建立客户端套接字 ## 创建UDP套接字
Client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

print('客户端socket对象----\n%s\n---type(Client_sock) is %s' % (Client_sock, type(Client_sock)))
#客户端socket对象----
#<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=17, laddr=('0.0.0.0', 0)>
#---type(Client_sock) is <class 'socket.socket'>


##第二步：发送数据
datastr = 'I am 客户端abc -- '
print('客户端未转换二进制的字符串信息-- %s\n' %  datastr)
#客户端未转换二进制的字符串信息--  I am 客户端abc --

databytes = bytes(datastr, encoding='utf8')
print("bytes(datastr, encoding='utf8'客户端发送的二进制信息是\n%s\n"  %  databytes)
#bytes(datastr, encoding='utf8'客户端发送的二进制信息是
#b'I am \xe5\xae\xa2\xe6\x88\xb7\xe7\xab\xafabc -- '

Client_sock.sendto(databytes, server_addr)
print('--------已经发送信息给了服务器---------')



##第 3 步：接收数据

server_data_bytes =  Client_sock.recv(1024)

print(server_data_bytes, end = '\n--注意服务端二进制信息server_data_bytes --\n')
#b'2019\xe5\xb9\xb4*04\xe6\x9c\x88*16\xe6\x97\xa5 18\xe6\x97\xb6:21\xe5\x88\x86:32\xe7\xa7\x92--\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe4\xbf\xa1\xe6\x81\xafI am \xe5\xae\xa2\xe6\x88\xb7\xe7\xab\xafabc -- '
#--注意服务端二进制信息server_data_bytes --


server_data_str = str(server_data_bytes, encoding= 'utf8')
print('\n接收的服务端信息转utf8字符串是\n', [server_data_str])
#接收的服务端信息转utf8字符串是
# ['2019年*04月*16日 18时:21分:32秒--服务器信息I am 客户端abc -- ']


#第4 步：关闭客户端套接字
Client_sock.close()




if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)






