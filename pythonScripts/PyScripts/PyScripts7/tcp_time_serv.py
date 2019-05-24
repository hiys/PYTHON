import socket
import time

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(2)
cli_sock, cli_addr = s.accept()
print('Client connected from:', cli_addr)
# 将收到的bytes类型，转成utf8字符串
data = str(cli_sock.recv(1024), encoding='utf8')
data = '[%s] %s' % (time.strftime('%H:%M:%d'), data)
# 发送时，将utf8字符串转成bytes类型
cli_sock.sendall(bytes(data, encoding='utf8'))
cli_sock.close()
s.close()
