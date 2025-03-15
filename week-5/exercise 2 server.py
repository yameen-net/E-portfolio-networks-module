import socket

# Create a UDP socket and bind it to localhost on port 65433.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Server is listening on port 65433...")

while True:
    data, client_address = server_socket.recvfrom(2048)
    print(f"Received from {client_address}: {data.decode()}")
    # Echo the data back to the sender.
    server_socket.sendto(b"ACK: " + data, client_address)
