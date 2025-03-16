import socket
import threading

def listen_for_messages(sock):
    """Continuously receive messages from the server and print them."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                # Server closed connection
                break
            print("Server:", data.decode())
        except Exception as e:
            print("Error receiving data:", e)
            break

def main():
    server_address = ('localhost', 65432)
    # TCP socket.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    print("Connected to server at", server_address)

    # dtart a thread
    listener = threading.Thread(target=listen_for_messages, args=(client_socket,))
    listener.daemon = True  #this makes sure the thread exits when the main program does.
    listener.start()

    #send messages to the server.
    while True:
        message = input("Enter message (or 'exit' to quit): ")
        if message.lower() == "exit":
            break
        client_socket.sendall(message.encode())

    client_socket.close()
    print("Disconnected from server.")

if __name__ == "__main__":
    main()
