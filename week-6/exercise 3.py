import ipaddress

#gold.ac.uk ip
ip_address = '159.100.136.66'

#analyze the IP address
ip = ipaddress.ip_interface(ip_address)

print(f"Address: {ip.ip}")
print(f"Network: {ip.network}")
print(f"Netmask: {ip.netmask}")
print(f"Is private: {ip.ip.is_private}")
print(f"Is global: {ip.ip.is_global}")
