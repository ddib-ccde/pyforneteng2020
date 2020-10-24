# Import regular expressions
import re

# Open file and read contents
with open("show_version.txt") as f:
    show_ver = f.read()

# Regex to extract IOS version, serial number and config register
ios_version = re.search(r"Version (\S+),", show_ver).group(1)
serial_num = re.search(r"^Processor board ID (\S+)", show_ver, flags=re.M).group(1)
config_reg = re.search(r"^Configuration register is (\S+)", show_ver, flags=re.M).group(1)

# Print information
print(f"OS Version: {ios_version}")
print(f"Serial Number: {serial_num}")
print(f"Config Register: {config_reg}")


