import socket
from cryptography.fernet import Fernet


#key
KEY = b'8bGV89kLEFgFDjWq9UZj1kUJ4PLQ37P1W--8E4Bty7M='
cipher_suite = Fernet(KEY)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Server is ready to receive encrypted messages...")

# authentication 
while True:
    data, client_address = server_socket.recvfrom(4096)
    
    # Decrypt 
    try:
        decrypted_message = cipher_suite.decrypt(data).decode()
        print(f"Decrypted message from {client_address}: {decrypted_message}")
    except Exception as e:
        print(f"Failed to decrypt message from {client_address}: {e}")
