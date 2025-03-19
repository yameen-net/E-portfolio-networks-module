import socket
import ipaddress

#getting host name and ip address
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(f"Your Computer Name is: {hostname}")
print(f"Your Computer IP Address is: {IPAddr}")

# analysing ip
ip = ipaddress.ip_interface(IPAddr)

print(f"Address: {ip.ip}")
print(f"Network: {ip.network}")
print(f"Netmask: {ip.netmask}")
print(f"Is private: {ip.ip.is_private}")
print(f"Is global: {ip.ip.is_global}")
