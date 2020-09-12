show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
# Strip white space from the string
show_version_strip = show_version.strip()
# Split the string into list consisting of three elements
show_version_split = show_version_strip.split()
# Grab model which is the second slice, meaning index 1
router_model = show_version_split[1]
# Grab serial number which is third slice, meaning index 2
router_serial = show_version_split[2]
# Check if Cisco, ignoring case, is in model
print(f"Is Cisco, ignoring case, in the model - {'cisco' in router_model.lower()}")
print(f"Is 881 in model - {'881' in router_model}")
# Print serial and model
print(f"{router_model}")
print(f"{router_serial}")