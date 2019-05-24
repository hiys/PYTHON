import socket

host = '127.0.0.1'
port = 12345
addr = (host, port)
c = socket.socket(type=socket.SOCK_DGRAM)

c.sendto(b'How are you?', addr)
print(c.recvfrom(1024))
c.close()
