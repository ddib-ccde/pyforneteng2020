# Open file and read lines into a list
with open("show_ip_int_brief.txt") as f:
    input = f.readlines()

# Get Fa4 info which is at index 5
list_line = input[5]

# Get the IP by using split and index 1
ip_addr = list_line.split()[1]

# Get the interface name at index 0
iface = list_line.split()[0]

# Create tuple
ip_info_tuple = (iface, ip_addr)

# Print tuple
print(ip_info_tuple)
