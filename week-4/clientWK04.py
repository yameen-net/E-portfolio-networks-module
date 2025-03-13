import socket
import threading

def listen_for_messages(client_socket):
    while True:
        data, _ = client_socket.recvfrom(2048)
        print("\n" + data.decode())

# Define server address and create a UDP socket
server_addr = ('localhost', 65433)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('', 0))  # OS assigns an available port

# Start a background thread to listen for messages from the server
listener = threading.Thread(target=listen_for_messages, args=(client_socket,))
listener.daemon = True
listener.start()

print("UDP Chat Client is running. Type messages to send:")

while True:
    msg = input()
    client_socket.sendto(msg.encode(), server_addr)
