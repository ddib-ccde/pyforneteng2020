# Import regular expression module
import re

# Open the file and read its contents
with open("show_ipv6_intf.txt") as f:
    show_ipv6 = f.read()

# Look for the IPv6 addresses using regex
match = re.search(r"IPv6 address:\s+(\S+)\s+\S+\s+(\S+)", show_ipv6, flags=re.DOTALL)

# Create IPv6 list
ipv6_list = []

# Append addresses to list
ipv6_list.append(match.group(1))
ipv6_list.append(match.group(2))

# Iterate over the list and print the contents
for ipv6_addr in ipv6_list:
    print(f"The IPv6 address is {ipv6_addr}")


