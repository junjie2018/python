import socket

s = socket.socket()
s.connect(("www.baidu.com", 80))
s.send(bytes("GET / HTTP/input.0 \r\n", encoding='utf-8'))
s.close()
print(s.recv(200))
