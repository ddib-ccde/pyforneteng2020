# Print an empty line
print(f"")
# Ask user for an IP address and store as string
ipaddr = input("Please enter an IP address: ")

# Split the IP address into four parts and store in a list
ipaddr_split = ipaddr.split(".")

# Print an empty line
print(f"")
# Print the header with centered text (^) and width 15
print(f"{'Octet1':^15}{'Octet2':^15}{'Octet3':^15}{'Octet4':^15}")
print("-" * 60)
# Print each octet of the IP address using list slicing
print(f"{ipaddr_split[0]:^15}{ipaddr_split[1]:^15}{ipaddr_split[2]:^15}{ipaddr_split[3]:^15}")
# Print IP in binary using builtin bin() function
# The ipaddr_split variable is a string, need to convert to integer with builtin function int()
print(
    f"{bin(int(ipaddr_split[0])):^15}"
    f"{bin(int(ipaddr_split[1])):^15}"
    f"{bin(int(ipaddr_split[2])):^15}"
    f"{bin(int(ipaddr_split[3])):^15}"
    )
# Print the IP in hex format using builtin function hex()
print(
    f"{hex(int(ipaddr_split[0])):^15}"
    f"{hex(int(ipaddr_split[1])):^15}"
    f"{hex(int(ipaddr_split[2])):^15}"
    f"{hex(int(ipaddr_split[3])):^15}"
    )    
print("-" * 60)