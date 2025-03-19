import socket

# defining the DHCP server and IP pool
server_ip = '127.0.0.1'
server_port = 12345
ip_pool = ['192.168.1.100', '192.168.1.101', '192.168.1.102']  # available IPs
leases = {}

def handle_client(client_socket):
    # step 2: Receive the DHCP Discover message from the client
    discover_msg = client_socket.recv(1024).decode('utf-8')
    print(f"server: Received: {discover_msg}")
    
    if discover_msg == 'DHCP Discover':
        # step 3: Offer an IP address to the client from the pool
        if ip_pool:
            offered_ip = ip_pool.pop(0)
            offer_msg = f"DHCPOffer {offered_ip}"
            client_socket.send(offer_msg.encode('utf-8'))
            print(f"server: Offered IP: {offered_ip}")
            
            # step 4: Receive DHCP Request from client
            request_msg = client_socket.recv(1024).decode('utf-8')
            print(f"server: Received: {request_msg}")
            
            if request_msg.startswith('DHCP Request'):
                assigned_ip = request_msg.split(' ')[2]
                leases[assigned_ip] = 'leased'
                ack_msg = f"DHCPAck {assigned_ip}"
                client_socket.send(ack_msg.encode('utf-8'))
                print(f"server: IP {assigned_ip} acknowledged and leased.")
            else:
                print("server: Invalid request received.")
        else:
            print("server: No IPs available!")
            client_socket.send("No IPs available".encode('utf-8'))
    client_socket.close()

# Setup the TCP server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)

print("server: Waiting for client connection...")
while True:
    client_socket, client_address = server.accept()
    print(f"server: Client connected from {client_address}")
    handle_client(client_socket)
