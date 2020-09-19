f = open("show_version.txt")
file = f.read()
print(file)
print(type(file))
f.close()

with open("show_version.txt") as f:
    content = f.readlines()

for line in content:
    print(line)
print(type(content))