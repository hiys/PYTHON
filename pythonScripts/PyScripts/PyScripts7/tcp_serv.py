import socket

host = ''   # 代表本机的所有IP地址
port = 12345  # 应该使用大于1024的值作为端口号
addr = (host, port)
s = socket.socket()
# 默认情况下，套接字被系统保留一分钟，程序结束后，１分钟内无法再次起动
# 设置地址重用，程序结束后，可以再立即运行
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)  # 绑定地址到套接字
s.listen(2)  # 起动监听，最多有两个客户端
cli_sock, cli_addr = s.accept()  # 开始等待客户端连接
print('Client connected from:', cli_addr)
data = cli_sock.recv(1024)  # 一次最多从客户机套接字接收1024字节
print([data])
cli_sock.close()
s.close()
# 客户端yum install -y telnet
# 客户端连接服务器 telnet 127.0.0.1 12345