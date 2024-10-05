import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 65432))

while True:
    data, addr = server.recvfrom(1024)
    filename = data.decode()

    if os.path.exists(filename):
        server.sendto("File exists".encode(), addr)
        with open(filename, 'rb') as file:
            data = file.read(1024)
            while data:
                server.sendto(data, addr)
                data = file.read(1024)
        server.sendto(b'EOF', addr)
    else:
        server.sendto("File does not exist".encode(), addr)
