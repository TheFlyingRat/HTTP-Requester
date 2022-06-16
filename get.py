

import socket
from socket import gethostbyname
import ssl


HOSTNAME = "ssh.theflyingrat.com"
TCP_IP = gethostbyname(HOSTNAME)
TCP_PORT = 443
BUFFER_SIZE = 2048
MESSAGE = ( 
            "GET / HTTP/1.1 \r\n"
            "Accept: */*\r\n"
            f"Host: {HOSTNAME}\r\n"
            "Scheme: https\r\n"
            "User-Agent: RatGetter v1.0\r\n"
            "Accept-Encoding: deflate, br\r\n\r\n"
            )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
ctx = ssl.SSLContext( ssl.PROTOCOL_TLSv1_2 )
s = ctx.wrap_socket(s, server_hostname=TCP_IP)
s.send(MESSAGE.encode())
data = s.recv(BUFFER_SIZE)
s.close()

with open("google.html", "w") as f:
    f.write(data.decode())