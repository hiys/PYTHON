import socket
import time
import threading

class TcpTimeServ:
    def __init__(self, host, port):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(2)

    def handle_child(self, cli_sock):
        while True:
            data = str(cli_sock.recv(1024), encoding='utf8')
            if not data.strip():
                break
            data = '[%s] %s' % (time.strftime('%H:%M:%d'), data)
            cli_sock.sendall(bytes(data, encoding='utf8'))
        cli_sock.close()

    def mainloop(self):
        while True:
            cli_sock, cli_addr = self.serv.accept()
            t = threading.Thread(target=self.handle_child, args=(cli_sock,))
            t.start()
        self.serv.close()

if __name__ == '__main__':
    s = TcpTimeServ('', 12345)
    s.mainloop()
