# Import pretty print
from pprint import pprint

# Open file and read lines
with open("show_arp.txt") as f:
    arp_entries = f.readlines()

# Remove first line by using slicing, index 1 to end
arp_entries = arp_entries[1:]

# Print list with pretty print
pprint(arp_entries)

# Sort the list
arp_entries.sort()

# Get first 3 entries
arp_first_three = arp_entries[:3]
arp_joined = "\n".join(arp_first_three)

# Open file and write to it
with open("arp_entries.txt", "w") as f:
    f.write(arp_joined)
