# Open file
f = open("show_version.txt")

# Read the file into a long string
file = f.read()

# Print the contents
print(file)
# Print the type
print(type(file))

# Close the file
f.close()

# Open file using file handle
with open("show_version.txt") as f:
    # Read the lines into a list
    content = f.readlines()

# Iterate over the list
for line in content:
    # Print each line in the list
    print(line)

# Print the type, should be list
print(type(content))