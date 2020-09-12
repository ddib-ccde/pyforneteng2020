mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

# Print empty line
print(f"")
# Print header, right aligned, 20 characters wide
print(f"{'IP ADDR':>20} {'MAC ADDRESS':>20}")
# Print 40 dashes
print(f"-" * 40)
# Print IP and MAC which is second and fourth slice, index 1 and 3
print(f"{mac1.split()[1]:>20} {mac1.split()[3]:>20}")
print(f"{mac2.split()[1]:>20} {mac2.split()[3]:>20}")
print(f"{mac3.split()[1]:>20} {mac1.split()[3]:>20}")