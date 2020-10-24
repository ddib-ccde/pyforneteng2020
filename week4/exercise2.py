# Create list for Houston IP addresses
houston_list = ["10.0.0.1", "10.0.1.254", "10.0.3.10", "172.16.0.1", "10.0.0.1",
"10.0.1.254", "192.168.0.1", "172.19.1.1", "10.0.4.1", "172.16.0.1"]

# Create list for Atlanta IP addresses
atlanta_list = ["10.0.0.1", "10.0.1.254", "172.16.0.1", "172.18.1.254", "10.10.10.10",
"10.100.0.1", "10.200.1.254", "172.20.1.1"]

# Create list for Chicago IP addresses
chicago_list = ["10.0.0.1", "172.19.1.1", "172.20.1.1", "10.103.1.1", "172.21.4.254",
"192.168.40.3", "192.168.202.1", "192.168.17.33"]

# Create set of all lists to remove any duplicates
houston_set = set(houston_list)
atlanta_set = set(atlanta_list)
chicago_set = set(chicago_list)

# Check what IP addresses are in both Houston and Atlanta
print(f"The duplicated IPs in Houston and Atlanta are {houston_set.intersection(atlanta_set)}")

# Find IPs that are duplicated in all sites
print(f"The duplicated IPs in Houston, Atlanta and Chicago are \
{houston_set.intersection(atlanta_set, chicago_set)}")

# Find unique IPs for Chicago
print(f"The unique IPs for Chicago are {chicago_set.difference(houston_set, atlanta_set)}")
