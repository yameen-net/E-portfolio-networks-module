
import socket

websites = ["google.com", "facebook.com", "twitter.com"]

for site in websites:
    try:
        ip = socket.gethostbyname(site)
        print(f"{site}: {ip}")
    except socket.gaierror:
        print(f"Could not resolve {site}")


import subprocess

def tracert(domain):
    try:
        result = subprocess.run(["tracert", domain], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("tracert command not found. Make sure it's available.")
    except Exception as e: # Catching general exceptions for now
        print(f"An error occurred: {e}")

domain = input("Enter the website or IP address: ")
tracert(domain)
