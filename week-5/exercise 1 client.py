import socket
import datetime


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))


message = input("Enter message: ")


#start time
start_time = datetime.datetime.now()

client_socket.sendall(message.encode())
response = client_socket.recv(1024)

#end time
end_time = datetime.datetime.now()

print(f"Server response: {response.decode()}")

#timetaken
time_taken = (end_time - start_time).total_seconds()
print("Time taken to send data:", time_taken, "seconds")

client_socket.close()
