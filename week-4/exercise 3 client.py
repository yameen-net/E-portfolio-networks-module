import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)

#username and password
username = input("Enter username: ")
password = input("Enter password: ")


auth_message = f"AUTH:{username}:{password}"
client_socket.sendto(auth_message.encode(), server_address)


response, _ = client_socket.recvfrom(2048)
if response.decode() == "AUTH_SUCCESS":
    print("Authentication successful! You can now start chatting.")
    
    
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break
        client_socket.sendto(message.encode(), server_address)
else:
    print("Authentication failed. Exiting.")

client_socket.close()
