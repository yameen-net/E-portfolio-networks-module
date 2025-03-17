import socket
import threading
from cryptography.fernet import Fernet

# key
SECRET_KEY = b's2x8bKT7Eli7OxPvcHrTf2WqlKhl9xcX9XwjF2fQpBU='
f = Fernet(SECRET_KEY)

clients = []  

def handle_client(client_socket, client_address):
    """Receive encrypted messages from one client, decrypt them, and broadcast to the other."""
    print(f"Connected to {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break  # client disconnected

            # decrypt the incoming message
            decrypted_message = f.decrypt(data).decode()
            print(f"From {client_address}: {decrypted_message}")

            # broadcast the decrypted message to other clients
            for c in clients:
                if c != client_socket:
                    encrypted_message = f.encrypt(f"Client {client_address}: {decrypted_message}".encode())
                    c.sendall(encrypted_message)

        except Exception as e:
            print(f"Error with {client_address}: {e}")
            break

    client_socket.close()
    clients.remove(client_socket)
    print(f"Connection closed for {client_address}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(2)  # accept only two clients for this chat
    print("Chat Server listening on port 65432...")

    while len(clients) < 2:
        # accept a new client connection
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

    print("Two clients are now connected. Chat is live!")

if __name__ == "__main__":
    main()
