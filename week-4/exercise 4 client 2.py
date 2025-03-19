import socket
from cryptography.fernet import Fernet

#key
KEY = b'8bGV89kLEFgFDjWq9UZj1kUJ4PLQ37P1W--8E4Bty7M='
cipher_suite = Fernet(KEY)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)

print("Enter your messages. Type 'exit' to quit.")
while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break
    
    # encrypt  before sending
    encrypted_message = cipher_suite.encrypt(message.encode())
    client_socket.sendto(encrypted_message, server_address)

client_socket.close()
