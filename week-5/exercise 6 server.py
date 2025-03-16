import socket
import threading

clients = []  # will hold the two connected client sockets

def handle_client(client_socket, client_address):
    """Receive messages from one client and broadcast them to the other."""
    print(f"Connected to {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                # client disconnected
                break
            
            message = data.decode()
            print(f"From {client_address}: {message}")

            # broadcast the message to the other client
            for c in clients:
                if c != client_socket:
                    c.sendall(f"Client {client_address}: {message}".encode())
        except Exception as e:
            print(f"Error with {client_address}: {e}")
            break
    
   
    client_socket.close()
    clients.remove(client_socket)
    print(f"Connection closed for {client_address}")

def main():
    # create a TCP socket and listen on localhost:65432
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(2)  # We'll only accept two clients for this chat
    print("Chat Server listening on port 65432...")

    while len(clients) < 2:
        # accept a new client connection
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        # start a thread 
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

    print("Two clients are now connected. Chat is live!")
    # the server continues running, handling clients in their respective threads
    
if __name__ == "__main__":
    main()
