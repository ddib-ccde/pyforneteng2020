# Import pretty print
from pprint import pprint

# Open the file and read the file into a string
with open("show_vlan.txt") as f:
    vlan_info = f.read()

# Initialize empty list for VLANs
vlan_list = []

# Iterate over the lines in vlan_info by using splitlines()
for line in vlan_info.splitlines():
    # Skip lines starting with VLAN, --- or empty line
    if "VLAN" in line or "---" in line or line.startswith("   "):
        continue
    vlan_id = line.split()[0]
    vlan_name = line.split()[1]
    vlan_list.append((vlan_id, vlan_name))

# Pretty print the VLAN list
pprint(vlan_list)