import ipaddress
import socket


def analyse_ip(ip_str):
    # Create an IP interface object from the string
    ip = ipaddress.ip_interface(ip_str)
    
    print(f"Address: {ip.ip}")
    print(f"Network: {ip.network}")
    print(f"Netmask: {ip.netmask}")
    print(f"Is private: {ip.ip.is_private}")
    print(f"Is global: {ip.ip.is_global}")
    
    # additional information based on CIDR
    print(f"Broadcast Address: {ip.network.broadcast_address}")

    print(f"First Usable IP: {list(ip.network.hosts())[0]}")

    print(f"Last Usable IP: {list(ip.network.hosts())[-1]}")

    print(f"Number of usable hosts: {ip.network.num_addresses - 2}")  # Subtract 2 for network and broadcast

    # list all hosts in the network but onlyu works for large networks
    if ip.network.num_addresses < 256:
        print("\nHosts in network:")
        for host in ip.network.hosts():
            print(host)

# Example usage
ip_str = '192.168.1.1/24'  
analyse_ip(ip_str)
