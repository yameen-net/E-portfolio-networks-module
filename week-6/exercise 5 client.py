import socket

# defining the client IP and port for the DHCP server
server_ip = '127.0.0.1'
server_port = 12345

def request_ip():
    # setup the TCP client to connect to the DHCP server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    
    # step 1: Send DHCP Discover message to the server
    discover_msg = 'DHCP Discover'
    client.send(discover_msg.encode('utf-8'))
    print("client: Sent: DHCP Discover")
    
    # step 2: Receive the DHCP Offer message from the server
    offer_msg = client.recv(1024).decode('utf-8')
    print(f"client: Received: {offer_msg}")
    
    if offer_msg.startswith('DHCPOffer'):
        # step 3: sending DHCP Request to the server to accept the offered IP
        requested_ip = offer_msg.split(' ')[1]
        request_msg = f'DHCP Request {requested_ip}'
        client.send(request_msg.encode('utf-8'))
        print(f"client: Sent: {request_msg}")
        
        # step 4: receiving the DHCP acknowledgment from the server
        ack_msg = client.recv(1024).decode('utf-8')
        print(f"client: Received: {ack_msg}")
    else:
        print("client: No offer received.")
    
    client.close()

#running function
request_ip()
