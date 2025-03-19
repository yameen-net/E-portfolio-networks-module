import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))

print("UDP Server is ready to receive messages...")

while True:
    data, client_address = server_socket.recvfrom(2048)  
    print(f"Received message from {client_address}: {data.decode()}")
    message = input("Reply: ")
    server_socket.sendto(message.encode(), client_address)  
