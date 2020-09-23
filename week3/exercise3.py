# Open file and read the lines into a string
with open("show_lldp_neighbors_detail.txt") as f:
    lldp_info = f.read()

# Set System Name and Port ID to None
system_name = None
port_id = None

# Iterate over the lines of the string lldp_info
for line in lldp_info.splitlines():
    # Check for Port ID
    if "Port id: " in line:
        # _ is a throw away variable
        _, port_id = line.split("Port id: ")
    # Check for System Name
    if "System Name: " in line:
        # _ is a throw away variable
        _, system_name = line.split("System Name: ")
    # If both are found, exit loop
    if port_id and system_name:
        break

# Print the information
print(f"The Port ID is {port_id} and the System Name is {system_name}")


