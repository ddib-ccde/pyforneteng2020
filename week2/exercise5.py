# Open and read file
with open("show_ip_bgp_summ.txt") as f:
    input = f.readlines()

# Get first line
first_line = input[0]

# Get last line
last_line = input[-1]

# Split first line to get AS, should be index 7
as_number = first_line.split()[7]

# Split last line to get peer IP, should be index 0
peer_ip = last_line.split()[0]

# Print the information
print(f"The AS number is {as_number} and the peer IP is {peer_ip}.")