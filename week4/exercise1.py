# Create dictionary for network device
network_device = {}
network_device["ip_addr"] = "192.0.2.1"
network_device["vendor"] = "Cisco"
network_device["username"] = "myuser"
network_device["password"] = "password"

# If vendor is Cisco, set platform to IOS, else if Juniper, set to JunOS
if "cisco" in network_device["vendor"].lower():
    network_device["platform"] = "ios"
elif "juniper" in network_device["vendor"].lower():
    network_device["platform"] = "junos"

# Create dictionary for BGP
bgp_fields = {}
bgp_fields["bgp_as"] = "64512"
bgp_fields["peer_as"] = "65000"
bgp_fields["peer_ip"] = "192.0.2.254"

# Use update to add bgp_fields dict key/value pairs to network device dict
network_device.update(bgp_fields)

# For loop to print keys of dictionary
for key in network_device:
    print(key)

# For loop to print key and value
for key, value in network_device.items():
    print(key)
    print(value)

