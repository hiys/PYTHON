import socket
import time

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(2)

while True:
    try:
        cli_sock, cli_addr = s.accept()
    except KeyboardInterrupt:
        break

    print('Client connected from:', cli_addr)
    while True:
        data = str(cli_sock.recv(1024), encoding='utf8')
        # if data.strip() == '':
        if not data.strip():
            break
        data = '[%s] %s' % (time.strftime('%H:%M:%d'), data)
        cli_sock.sendall(bytes(data, encoding='utf8'))
    cli_sock.close()
s.close()
