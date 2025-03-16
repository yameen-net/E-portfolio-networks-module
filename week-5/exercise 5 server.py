import socket
import threading

def handle_client(client_socket, client_address):
    """Receive data from a client and echo it back."""
    print(f"Connected to {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                # break when no data
                break
            print(f"Received from {client_address}: {data.decode()}")
            # Echo the received data back to the client
            client_socket.sendall(b"ACK: " + data)
        except Exception as e:
            print(f"Error with {client_address}: {e}")
            break
    client_socket.close()
    print(f"Connection closed for {client_address}")

def start_server():
    """Starts the TCP server and handles multiple client connections."""
    # TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(5)  # max 5 queued connections
    print("TCP Server is listening on port 65432...")

    while True:
        # Accept a new client connection.
        client_socket, client_address = server_socket.accept()
        # Start a new thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.daemon = True  # so threads exit when the main program exits
        client_thread.start()

if __name__ == "__main__":
    start_server()
