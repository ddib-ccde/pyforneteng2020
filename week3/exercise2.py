# Open the file and read it into a string
with open("show_arp.txt") as f:
    arp_file = f.read()

# Define variables used for identifying if 88.1 and 88.30 have been found
found1 = False
found2 = False

# Iterate over contents in arp_file by splitting lines into a list
for line in arp_file.splitlines():
    # Skip the line with protocol in it
    if "protocol" in line.lower():
        continue
    # Get the IP addr which is at index 1
    ip_addr = line.split()[1]
    # Get the MAC addr which is at index 3
    mac_addr = line.split()[3]
    # If 88.1 is found, print information about GW
    if "10.220.88.1" in ip_addr:
        print(f"Default gateway IP/MAC: {ip_addr:^5} {mac_addr:^5}")
        found1 = True
    # If 88.30 is found, print information about Arista3
    if "10.220.88.30" in ip_addr:
        print(f"Arista3 IP/MAC is {ip_addr:^5} {mac_addr:^5}")
        found2 = True
    # Check if both have been found
    if found1 and found2:
        print(f"Exiting loop now...")
        break


