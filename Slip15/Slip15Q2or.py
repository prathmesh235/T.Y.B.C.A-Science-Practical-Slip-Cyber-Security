ip_locations = {
    "192.168.1.1": "Pune",
    "192.168.1.2": "Mumbai",
    "192.168.1.3": "Nashik",
    "192.168.1.4": "Delhi"
}

ip = input("Enter an IP address: ")

if ip in ip_locations:
    print("Location:", ip_locations[ip])
else:
    print("IP address not found.")
