import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Server waiting for authentication...")

# valid credentials
VALID_USERNAME = "user1"
VALID_PASSWORD = "password123"

# authentication 
while True:
    data, client_address = server_socket.recvfrom(2048)
    message = data.decode().strip()
    
   
    if message.startswith("AUTH:"):
        parts = message.split(":")
        if len(parts) == 3:
            username = parts[1]
            password = parts[2]
            if username == VALID_USERNAME and password == VALID_PASSWORD:
                server_socket.sendto("AUTH_SUCCESS".encode(), client_address)
                print(f"Authentication successful for {username} from {client_address}")
                break  
            else:
                server_socket.sendto("AUTH_FAILED".encode(), client_address)
                print(f"Authentication failed for {username} from {client_address}")
        else:
            server_socket.sendto("AUTH_FAILED".encode(), client_address)
    else:
       
        server_socket.sendto("Please authenticate using format AUTH:username:password".encode(), client_address)

print("Now entering chat mode...")


while True:
    data, client_address = server_socket.recvfrom(2048)
    print(f"Received from {client_address}: {data.decode()}")
