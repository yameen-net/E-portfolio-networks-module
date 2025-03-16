import socket
import datetime

server_address = ('localhost', 65433)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file_path = "file_to_send_udp.txt"  # Ensure this file exists and contains your text.

# Record the start time before sending.
start_time = datetime.datetime.now()

with open(file_path, "rb") as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        client_socket.sendto(chunk, server_address)

# Send an EOF marker to signal the end of the file.
client_socket.sendto("EOF".encode(), server_address)

# Record the end time after sending.
end_time = datetime.datetime.now()

time_taken = (end_time - start_time).total_seconds()
print(f"File '{file_path}' sent in {time_taken} seconds.")

client_socket.close()
