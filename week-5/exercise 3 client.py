import socket

# Define the server address and port.
server_address = ('localhost', 65432)

# Create a TCP socket.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# Open the text file you want to send in binary mode.
with open("file_to_send.txt", "rb") as f:
    data = f.read()
    # Send the entire file content to the server.
    client_socket.sendall(data)

print("File data sent to the server.")

client_socket.close()
