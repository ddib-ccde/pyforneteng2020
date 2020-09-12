# Define IPv6 addresses
ip_address = "2001:db8:1234:1234::1"
IP_ADDR = "2001:db8:1234:1234::2"
ipv6_address = "2001:db8:1234:1234::3"

# Compare if first variable equals second variable
print(f"Is {ip_address} = {IP_ADDR} - {ip_address == IP_ADDR}")
# Compare if first variable is not equal to third variable
print(f"Is {ip_address} != {IP_ADDR} - {ip_address != ipv6_address}")