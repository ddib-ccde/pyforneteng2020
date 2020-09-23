# List of tuples consisting of IP and MAC
arp_table = [('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')]

 # Iterate over the list of tuples using unpacking
for ip_addr, mac_addr in arp_table:
    # Remove the dot from MAC by splitting and then joining
    mac_addr = mac_addr.split(".")
    mac_addr = "".join(mac_addr)
    # Convert to upper case
    mac_addr = mac_addr.upper()
    # Empty list to store the new MAC
    new_mac = []
    # Split MAC to be 2 chars long
    while len(mac_addr) > 0:
        # Get first 2 chars
        entry = mac_addr[:2]
        # Remove first 2 chars from mac_addr
        mac_addr = mac_addr[2:]
        # Append to the list new_mac
        new_mac.append(entry)
    # Join the MAC with colon
    new_mac = ":".join(new_mac)
    # Print the MAC
    print(new_mac)


