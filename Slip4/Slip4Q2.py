#Q.2. Write a Python program to demonstrate IP tracking simulation by storing fake IP addresses and printing location mapping using a dictionary
ip_locations = {
    "192.0.2.1": "Mumbai",
    "192.0.2.2": "Pune",
    "192.0.2.3": "Delhi",
    "192.0.2.4": "Nashik"
}
ip = input("Enter IP address: ")
if ip in ip_locations:
    print("Location:", ip_locations[ip])
else:
    print("IP address not found.")
