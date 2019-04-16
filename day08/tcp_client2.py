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

import  sys, socket, time

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)


host_server_ip = '192.168.1.10'    #'192.168.1.10'是服务器的ip 地址
server_port = 11200       #使用大于 1024的值作为端口号,注意要和服务端的端口一样
addr = (host_server_ip, server_port)  #作为一个元组类型的数据


##第一步：建立socket对象
#使用给定的地址族，套接字类型 和 协议号来创建一个新套接字
#socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP )
print('客户端socket对象是---- \n%s\n---type(client_sock) is %s' \
  % (client_sock, type(client_sock)))
#客户端socket对象是---- 
#<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('0.0.0.0', 0)>
#---type(client_sock) is <class 'socket.socket'>


##第二步：绑定服务端的ip地址和服务端端口链接服务器
client_sock.connect(addr)


#第3-4步,处理阶段，服务器与客户端通过send和recv方法通信(传输数据)
#调用套接字client_sock 与 服务器通信
#第三步: 发送数据到服务器
client_sock.sendall(b'I am bytes info\r\n')

#第4 步,接收服务端的数据
fromserver_databytes = client_sock.recv(1024) #接收服务端信息，一次接收数据的大小最多是1024字节

print('接收的服务端[二进制]信息是\n %s \n type is --**--%s' %  ([fromserver_databytes],type(fromserver_databytes)))
#接收的服务端信息是
# [b'[2019\xe5\xb9\xb4*04\xe6\x9c\x88*15\xe6\x97\xa5 21\xe6\x97\xb6:07\xe5\x88\x86:24\xe7\xa7\x92] I am bytes info\r\n'] 
# type is --**--<class 'bytes'>

server_datastr =  str(fromserver_databytes, encoding='utf8') #将服务器发送的二进制文字转utf8字符串格式
print('\n注意如果服务器执行 Ctrl + C会发生二进制文字转换错误UnicodeDecodeError\n')
print('---接受的服务器---信息转utf8字符串格式\n', server_datastr, end ='')

#第5步,传输结束，关闭链接
client_sock.close() #关闭客户端链接




if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)




