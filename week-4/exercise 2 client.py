import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)

while True:
    message = input("You: ")
    client_socket.sendto(message.encode(), server_address)
    
    if message.lower() == 'exit':  
        print("Exiting chat...")
        break
    
    data, server = client_socket.recvfrom(2048)
    print(f"Server: {data.decode()}")  

client_socket.close()
