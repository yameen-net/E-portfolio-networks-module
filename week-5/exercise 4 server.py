import socket

#UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Server is listening on port 65433...")


with open('received_file_udp.txt', 'wb') as f:
    while True:
        data, client_address = server_socket.recvfrom(1024)
        # Check for our end-of-file marker
        if data.decode() == "EOF":
            print("Received EOF marker. File transfer complete.")
            break
        f.write(data)
        print(f"Received {len(data)} bytes from {client_address}")

server_socket.close()