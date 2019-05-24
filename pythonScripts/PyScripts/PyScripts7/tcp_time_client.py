import socket
import sys

class TcpTimeClient:
    def __init__(self, host, port):
        self.addr = (host, port)
        self.cli = socket.socket()
        self.cli.connect(self.addr)

    def chat(self):
        while True:
            data = input('> ')
            data = bytes(data, encoding='utf8')
            self.cli.sendall(data)
            if not data:
                break
            print(str(self.cli.recv(1024), encoding='utf8'))
        self.cli.close()

if __name__ == '__main__':
    c = TcpTimeClient(sys.argv[1], int(sys.argv[2]))
    c.chat()
