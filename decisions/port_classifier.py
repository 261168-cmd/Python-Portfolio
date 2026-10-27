# port_classifier.py
# Description: This program checks port numbers, finds their ranges, and identifies services.

# Ask the user to type a port number
port = int(input("Port: "))

# Check if the port number is wrong (out of limits)
if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535.")
else:
    # Check the group of the port (system, user, or dynamic)
    if port <= 1023:
        port_range = "system"
    elif port <= 49151:
        port_range = "user"
    else:
        port_range = "dynamic or private"
        
    print(f"Range: {port_range}")
    
    # Check if the port is for ssh, http, or https
    if port == 22:
        print("Service: ssh")
    elif port == 80:
        print("Service: http")
    elif port == 443:
        print("Service: https")

# --- END OF PROGRAM ---
