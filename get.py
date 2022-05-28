

import socket
from socket import gethostbyname


HOSTNAME = "theflyingrat.com"
TCP_IP = gethostbyname(HOSTNAME)
TCP_PORT = 80
BUFFER_SIZE = 2048
MESSAGE = (
            "GET / HTTP/1.1\r\n"
            "Accept: */*\r\n"
            f"Host: {HOSTNAME}\r\n"
            "User-Agent: RatGetter v1.0\r\n"
            "Accept-Encoding: gzip, deflate, br\r\n\r\n"
            )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
data = s.recv(BUFFER_SIZE)
s.close()

print(data.decode())