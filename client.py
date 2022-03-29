import socket
import sys

HOST = '168.122.216.154'  # The server's hostname or IP address
PORT = 8081 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    message = sys.stdin.readline().encode()
    s.send(message)

    # s.send(b"Hello, world")
    
    data = s.recv(1024)

print(f"Received {data!r}")