import socket
import threading
from cryptography.fernet import Fernet

# key
SECRET_KEY = b's2x8bKT7Eli7OxPvcHrTf2WqlKhl9xcX9XwjF2fQpBU='
f = Fernet(SECRET_KEY)

def listen_for_messages(sock):
    """Continuously receive encrypted messages, decrypt, and print them."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break  

            # decrypt the message received from the server
            decrypted_message = f.decrypt(data).decode()
            print("\n" + decrypted_message)

        except Exception as e:
            print("Error receiving data:", e)
            break

def main():
    server_ip = 'localhost'
    server_port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")
    print("Type your messages below (type 'exit' to quit):")

    # sdtart a thread 
    thread = threading.Thread(target=listen_for_messages, args=(client_socket,))
    thread.daemon = True
    thread.start()

    while True:
        message = input()
        if message.lower() == "exit":
            break

        # Encrypt the message before sending it to the server
        encrypted_message = f.encrypt(message.encode())
        client_socket.sendall(encrypted_message)

    client_socket.close()
    print("Disconnected from server.")

if __name__ == "__main__":
    main()
