import socket

# Create a UDP socket and bind it to localhost on port 65433
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Chat Server is running on port 65433...")

# Dictionary to store client addresses
clients = {}

while True:
    data, client_addr = server_socket.recvfrom(2048)
    message = data.decode()
    
    # Add the client address if not already present
    clients[client_addr] = True
    print(f"Received from {client_addr}: {message}")
    
    # Broadcast the message to all other clients
    for addr in clients:
        if addr != client_addr:
            server_socket.sendto(data, addr)
