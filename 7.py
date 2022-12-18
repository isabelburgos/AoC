file = open("input7.txt","r")


directories = {}
current_dir = ""
listing = False
current_size = 0
for line in file:
    if line.split()[0] == "$":
        listing = False
        command = line.split()[1:]
        if command[0] == "cd":
            dest = command[1]
            if dest == '..':
                current_dir = "/".join((current_dir.split("/"))[0:-1])
            else:
                current_dir += "/" + dest
        if command[0] == "ls":
            listing = True
            continue
    if listing:
        result = line.split()
        if result[0] == "dir":
            directory = result[1]
            continue
        else:
            size = result[0]
            filename = result[1]
            current_size = int(size)
    if not current_dir in directories.keys():
        directories.update({current_dir:0})
    else:
        subpaths = current_dir.strip("///").split("/")
        if subpaths[0] == '':
            subpaths[0] = "//"
        else:
            subpaths = ["//"] + subpaths
        pathlength = len(subpaths)
        for n in range(0,pathlength):
            path = "/".join(subpaths[:n+1])
            directories[path] += current_size
        current_size = 0

total = 0
for val in list(directories.values())[1:]:
    if val <= 100000:
        total += val
print(total)

space_needed = 30000000
total_disk_space = 70000000
space_used = directories["//"]
space_remaining = total_disk_space - space_used
space_to_free = space_needed - space_remaining

minimum = [space_used,"//"]
for directory in directories:
    space = directories[directory]
    if space > space_to_free:
        if space < minimum[0]:
            minimum = [space,directory]

print(minimum[0])