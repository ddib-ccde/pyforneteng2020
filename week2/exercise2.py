# Create list of five IP addresses
my_ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4", "10.0.0.5"]
# Append one address to list
my_ip_addresses.append("192.0.2.1")
# Use extend to add another two addresses
my_ip_addresses.extend(["172.16.0.1", "172.16.0.2"])
# Concatenate to add two addresses
my_ip_addresses += ["192.168.0.1", "192.168.0.2"]
# Print the list of IPs
print(my_ip_addresses)
# Remove first IP
my_ip_addresses.pop(0)
# Remove last IP
my_ip_addresses.pop()
# Change first IP to be 2.2.2.2
my_ip_addresses[0] = "2.2.2.2"
# Print first IP
print(my_ip_addresses[0])
