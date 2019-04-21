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

import  sys, socket, time, threading

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)


class  TcpTimeServer:
  def  __init__(self, host_ip='', port= 11200):
    """host_ip = '' #空字符串''代表本机的所有ip 地址"""

    self.date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
    self.ser_addr_ip_port = (host_ip, port)  #作为一个元组类型的数据
##第一步：建立socket对象
#使用给定的地址族，套接字类型 和 协议号来创建一个新套接字
#socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
    self.servSocketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP )
    print('服务器socket对象是\n%s\n---type(s) is %s' % (self.servSocketObj, type(self.servSocketObj)))

##第二步：设置socket选项
#最后一个参数value 数字1代表 True  或者数字0代表 False
    self.servSocketObj.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEADDR, 1)

#第三步：绑定socket
    self.servSocketObj.bind(self.ser_addr_ip_port)  #绑定主机ip地址和端口号

#第4 步：侦听连接
    self.servSocketObj.listen(2)   #启动监听ip地址端口, 一次同时最多有2 个客户端连接请求


#第六步,处理阶段，服务器与客户端通过send和recv方法通信(传输数据)
#调用新链接对象cli_sock 与客户端cli_addr 或者服务器通信
  def  handle_child(self,cli_sock):
    while  True:
      try:
        databytes = cli_sock.recv(1024) #接收客户端信息，一次接收数据的大小最多是1024字节
      except  KeyboardInterrupt:
        print('--- 在接收客户端信息的时候服务端Ctrl + C 将会退出客户端与服务端的对话程序!')  
        break
      print('接受的客户端二进制信息是\n', [databytes])
#接受的客户端二进制信息是
# [b'\t']
# [b'']

      try:
        datastr = str(databytes, encoding='utf8')  #将客户端发送的二进制文字转utf8字符串格式

      except   UnicodeDecodeError  as  ue :
        print('\n客户端执行 Ctrl + C会发生错误UnicodeDecodeError\n', ue)
        break
      print('---接受的客户端信息转utf8字符串格式\n', datastr)

      if  not datastr.strip(): #如果客户端输入任意连续的空字符(包括\r\v\t 空格)
        break
      data = '[%s] %s' % (self.date, datastr)  #注意这里的属性日期变量date

#服务端V0调用新链接对象 cli_sock 发送二进制信息bytes(data, encoding='utf8')给客户端
      serverV0 = cli_sock.sendall(bytes(data, encoding='utf8'))
      print('cli_sock.sendall()--serverV0返回信息\n%s---%s' %  (serverV0, type(serverV0)))
#cli_sock.sendall()--serverV0返回信息
#None---<class 'NoneType'>

#第七步,传输结束，关闭链接
    cli_sock.close() #关闭客户端链接 #注意逻辑层次,缩进格式
    print('\n本次服务端与客户端的对话结束,可以开启下一个新的对话连接\n')


  def  mainloop(self):
    while  True:
      try:
#第 5 步: 阻塞等待链接请求self.servSocketObj.accept()
#服务器通过 新的socket对象cli_sock 与客户端通信
        cli_sock, cli_addr = self.servSocketObj.accept() #阻塞等待客户端的链接请求
      except  KeyboardInterrupt:
        print('---在服务端阻塞等待客户端的链接请求时Ctrl + C 将会退出客户端与服务端的对话程序!')
        break
      print('socket套接字对象cli_sock是  ', cli_sock)      
      print('Client address is cli_addr connect from :\n ', cli_addr)


#第六步,处理阶段，服务器与客户端通过send和recv方法通信(传输数据)
#      self.handle_child(cli_sock)
      thr = threading.Thread(target=self.handle_child, args = (cli_sock,))
      thr.start()

#第七步,传输结束，关闭链接
#    cli_sock.close() #关闭客户端链接
#    print('\n本次服务端与客户端的对话结束,可以开启下一个新的对话连接\n')

#第八步,传输结束，关闭链接
    self.servSocketObj.close() #关闭服务端(本地主机)链接



if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  server_SocketObj = TcpTimeServer()
  server_SocketObj.mainloop()



