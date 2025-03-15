import socket
import datetime

#udp socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65432)

message = input("Enter message: ")

#start time.
start_time = datetime.datetime.now()

# sending message to server
client_socket.sendto(message.encode(), server_address)

# server responce 
data, _ = client_socket.recvfrom(2048)

# endtime
end_time = datetime.datetime.now()

print("Server response:", data.decode())

# calculate and display the round-trip time
time_taken = (end_time - start_time).total_seconds()
print("Time taken to send data using UDP:", time_taken, "seconds")

client_socket.close()
