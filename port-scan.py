import socket
import sys
from datetime import datetime

# Define the target
if len(sys.argv) != 2:
    print("Usage: python3 port_scan.py <target>")
    sys.exit(1)

target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4

# Display the scanning information
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # Scan ports 1-1024
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit(0)
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit(1)
except socket.error:
    print("\nCouldn't connect to server.")
    sys.exit(1)

print("-" * 50)
print("Scanning completed.")
print("-" * 50)
