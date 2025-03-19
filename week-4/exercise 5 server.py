import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Server listening on port 65433...")

while True:
    data, addr = server_socket.recvfrom(4096)
    print("Received from", addr, ":", data.decode())
