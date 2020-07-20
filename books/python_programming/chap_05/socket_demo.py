import sys
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

port = 50008
host = 'localhost'


def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        reply = 'server got: [%s]' % data
        conn.send(reply.encode())


def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply = sock.recv(1024)
    sock.close()
    print('client go: [%s]' % reply)


def child_main():
    for i in range(5):
        Thread(target=client, args=('client%s' % i,)).start()


if __name__ == '__main__':
    eval(sys.argv[1])()
