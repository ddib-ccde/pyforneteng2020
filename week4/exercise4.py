# Import regular expressions module
import re
show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''
# Search for string starting with Cisco and non white space
match = re.search(
    r"Cisco (?P<model>\S+).* with (?P<memory>\S+) bytes",
    show_version,
    flags=re.M,
)

# Use groupdict to access information
model = match.groupdict()["model"]
memory = match.groupdict()["memory"]

# Print information
print(f"Model: {model}")
print(f"Memory: {memory}")
