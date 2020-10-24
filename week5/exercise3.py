# Function to normalize MAC addresses
def normalize_mac(mac_address):
    # Convert MAC to upper case
    mac_address = mac_address.upper()

    # If MAC has colon, split on colon
    if ":" in mac_address:
        # List to store MAC address
        new_mac = []
        mac_list = mac_address.split(":")
        # Pad with zeroes if needed, using zfill
        for list_entry in mac_list:
            # Check if each entry in list has 2 chars or not
            if len(list_entry) < 2:
                list_entry = list_entry.zfill(2)
            new_mac.append(list_entry)
                
    # If MAC has dash, split on dash
    if "-" in mac_address:
        # List to store MAC address
        new_mac = []
        mac_list = mac_address.split("-")
        # Pad with zeroes if needed, using zfill
        for list_entry in mac_list:
            # Check if each entry in list has 2 chars or not
            if len(list_entry) < 2:
                list_entry = list_entry.zfill(2)
            new_mac.append(list_entry)
    
    # If MAC has dot, split on dot
    elif "." in mac_address:
        # List to store MAC address
        new_mac = []
        mac_list = mac_address.split(".")
        # Check if there are three sections, raise ValueError, if needed
        if len(mac_list) != 3:
            raise ValueError("Not a valid format")
        for list_entry in mac_list:
            # Check that there are 4 chars, otherwise fill with zfill
            if len(list_entry) < 4:
                list_entry = list_entry.zfill(4)
            # Append first 2 chars to the list
            new_mac.append(list_entry[:2])
            # Append last 2 chars to the list
            new_mac.append(list_entry[2:])
    
    # Return MAC address joined by :
    return ":".join(new_mac)

# Test that function works
assert "01:23:02:34:04:56" == normalize_mac("123.234.456")
assert "AA:BB:CC:DD:EE:FF" == normalize_mac("aabb.ccdd.eeff")
assert "0A:0B:0C:0D:0E:0F" == normalize_mac("a:b:c:d:e:f")
assert "01:02:0A:0B:03:44" == normalize_mac("1:2:a:b:3:44")
assert "0A:0B:0C:0D:0E:0F" == normalize_mac("a-b-c-d-e-f")
assert "01:02:0A:0B:03:44" == normalize_mac("1-2-a-b-3-44")
