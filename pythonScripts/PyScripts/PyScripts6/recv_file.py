import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(2)
cli_sock, cli_addr = s.accept()
print('Client connected from:', cli_addr)
data = cli_sock.recv(10)
data += cli_sock.recv(10)
print([data])
cli_sock.close()
s.close()
