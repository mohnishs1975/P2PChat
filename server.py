import socket

# Create socket
ADDRESS = '168.122.216.154'
PORT = 8081
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ADDRESS,PORT))
server.listen()

conn, addr = server.accept()

with conn:
    print(f"Connected by {addr}")
    while True:
            data = conn.recv(1024)
            print(f"Received: {data}")
            if not data:
                break
            conn.sendall(data)

