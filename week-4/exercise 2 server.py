import socket

# dictionary to store user IPs and usernames
user_dict = {}


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))

print("UDP Server is ready to receive messages...")

while True:
    data, client_address = server_socket.recvfrom(2048) 
    
    
    client_ip = client_address[0]
    
    if client_ip not in user_dict:
        # ask for their username
        username = input(f"New user connected from {client_ip}. Please enter a username: ")
        user_dict[client_ip] = username  # store the username with the client's IP as the key
    
    print(f"User {user_dict[client_ip]} (IP: {client_ip}) sent: {data.decode()}")
    
   
    message = input("Reply: ")
    server_socket.sendto(message.encode(), client_address)  
