import socket

host = '127.0.0.1'
port = 12345
addr = (host, port)
c = socket.socket()
c.connect(addr)
c.sendall(b'I C U.')
print(str(c.recv(1024), encoding='utf8'), end='')
c.close()
