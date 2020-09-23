# Import OS to be able to ping
import os
# Change to true on OS is Windows
WINDOWS = False

base_cmd_linux = "ping -c 2"
base_cmd_windows = "ping -n 2"
# Ternary operator to pick base command
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

# Create the base IP
base_ip = "192.168.255."
# Create empty IP list
ip_list = []
# Use For loop with range to add IP addresses to list
for ip in range(1, 255):
    # Concatenate base_ip and string version of iterator ip
    ip_addr = base_ip + str(ip)
    # Append to the list
    ip_list.append(ip_addr)

# Print all addresses using enumerate
for index, ip in enumerate(ip_list):
    print(f"{index} ---> {ip}")

# Use list slice to get two IP addresses
new_ip_list = ip_list[10:12]

# Use For loop to ping IP addresses in new_ip_list
for ip in new_ip_list:
    # os.system to send commands, f-string to combine base_cmd and iterator ip
    os.system(f"{base_cmd} {ip}")


