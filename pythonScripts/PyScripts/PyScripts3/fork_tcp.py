#!/usr/bin/env python
#coding: utf-8
import os
import time
import socket


#服务器IP，通常为空字符串
host = ‘‘
#端口号
port = 21345
#在AF_INET下,以元组（host,port）的形式表示地址
addr = (host,port)

#创建TCPsocket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置选项
#value为1，表示将SO_REUSEADDR标记为TRUE
#操作系统会在服务器socket关闭或服务进程终止后马上释放服务器端口
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#将套接字绑定到地址
s.bind(addr)
#侦听连接 允许一个连接在队列中等待
s.listen(1)

while True:
    try:
        while True:
			#获取waitpid的返回值
			#有三种情况
			#当正常返回的时候，waitpid返回收集到的子进程的进程ID
			#如果设置了选项WNOHANG，而调用中waitpid发现没有已退出的子进程可收集，则返回0
			#如果调用中出错，则返回-1
            result = os.waitpid(-1,os.WNOHANG)
            if result[0] == 0:
                break
	#防止出错导致程序终止
    except OSError:
        pass
	#accept()接受TCP连接并返回（conn,address）
	#conn是新的套接字对象，可以用来接收和发送数据。
	#address是连接客户端的地址。
    cli_sock,cli_addr = s.accept()
    pid = os.fork()
    if pid:
		#父进程
		#关闭接收和发送数据的套接字
        cli_sock.close()
    else:
        s.close()
        while True:
			#接受TCP套接字的数据 最大4096
            data = cli_sock.recv(4096)
			#如果空白字符串退出
            if not data.strip():
                cli_sock.close()
                sys.exit()
			#添加时间戳
            cli_sock.send("[%s] %s" % (time.ctime(),data))
        cli_sock.close()
s.close()