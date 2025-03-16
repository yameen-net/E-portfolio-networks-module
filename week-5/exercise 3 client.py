import socket
import datetime



# Define the server address and port.
server_address = ('localhost', 65432)

# Create a TCP socket.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)



# Open the text file you want to send in binary mode.
with open("file_to_send.txt", "rb") as f:
    data = f.read()
    # Send the entire file content to the server.

    start_time = datetime.datetime.now()
    client_socket.sendall(data)

end_time = datetime.datetime.now()

time_taken = (end_time - start_time).total_seconds()

print(f"File data sent to the server taking {time_taken} seconds")

client_socket.close()
