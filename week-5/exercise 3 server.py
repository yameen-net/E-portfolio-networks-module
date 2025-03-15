import socket

#TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))
server_socket.listen(1)  
print("TCP Server is listening on port 65432...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")
    
    
    with open('received_file.txt', 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
    print("Data logged to 'received_file.txt'")
    client_socket.close()