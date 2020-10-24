# Function for connecting via SSH
def ssh_conn(ip_addr, username, password):
    # print information
    print(f"IP address: {ip_addr}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    # Print an empty line
    print("")

# Call function using positional arguments
ssh_conn("10.0.0.1", "admin", "admin")

# Call function using named arguments
ssh_conn(ip_addr="172.16.0.1", username="netadmin", password="cisco123")

# Call using a mix of positional and named
ssh_conn("192.168.0.1", username="cisco", password="secret")
