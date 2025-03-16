import socket
import threading

def listen_for_messages(sock):
    """Continuously receive messages from the server and print them."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                
                break
            print("\n" + data.decode())
        except:
            break

def main():
    server_ip = 'localhost'
    server_port = 65432

    # TCP socket 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")
    print("Type your messages below (type 'exit' to quit):")

    # Start a thread 
    thread = threading.Thread(target=listen_for_messages, args=(client_socket,))
    thread.daemon = True
    thread.start()

    
    while True:
        message = input()
        if message.lower() == "exit":
            break
        client_socket.sendall(message.encode())

    client_socket.close()
    print("Disconnected from server.")

if __name__ == "__main__":
    main()
