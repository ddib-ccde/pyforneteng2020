# Function for connecting via SSH
def ssh_conn(ip_addr, username, password, device_type="cisco_ios"):
    # print information
    print(f"IP address: {ip_addr}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Device type: {device_type}")
    # Print an empty line
    print("")

# Call function specifying device type
ssh_conn("10.0.0.1", "admin", "admin", device_type="arista")

# Call function not specifying device type
ssh_conn("10.0.0.1", "admin", "cisco123")

# Create dictionary to use in call to function
device_dict = {
    "ip_addr": "172.16.0.1",
    "username": "netadmin",
    "password": "junos123",
    "device_type": "junos",
}

# Call function with unpacking dict
ssh_conn(**device_dict)
